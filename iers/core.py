import os
import numpy as np
import pandas as pd
from urllib.request import urlretrieve
from datetime import datetime
from .time import iso2dt, dt_to_mjd


##def self.__extract(line, i1, i2):
##    tmp = line[i1-1:i2]
##    if tmp.strip().replace('.','').replace('-','').isdigit():
##        return float(tmp)
##    else:
##        np.nan


class EOP:
    def __init__(self, kind=1):
        self.kind = kind
        self.table = None
        self.bulletin = None
        
        if self.kind == 4:
            self.BASE = 'https://hpiers.obspm.fr/iers/series/longterm/'
        elif kind in [1,2,3]:
            self.BASE = 'https://datacenter.iers.org/data/latestVersion/'
        else:
            raise Exception('kind must be 1, 2, 3 or 4')
        self.path = os.path.expanduser('~/Documents/')
        self.__trim = {}
        if self.kind == 1:
            self.FileName = 'finals.all.iau2000.txt'
        elif self.kind == 2:
            self.FileName = 'EOP_14_C04_IAU2000A_one_file_1962-now.txt'
            self.__trim = {'lines':13, 'mjd':(14,19)}
            self.__trim.update({'px':(21,30), 'py':(32,41), 'ut1_utc':(43,53), 'lod':(55,65), 'dx':(67,76), 'dy':(78,87)}) #OK
        elif self.kind == 3:
            self.FileName = 'EOP_C01_IAU2000_1846-now.txt'
            self.__trim = {'lines':13, 'mjd':(3,12)}
            self.__trim.update({'px':(13,22), 'py':(23,32), 'ut1_tai':(33,44), 'dx':(49,58), 'dy':(62,71), 'lod':(228,237)})#OK
        elif self.kind == 4:
            self.FileName = 'nao_a.eop'
            self.__trim = {'lines':13, 'mjd':(0,13)}
            self.__trim.update({'ut1_tai': (33,48), 'lod': (229,238)})

        self.URL = self.BASE + self.FileName
        self.columns = [i for i in self.__trim.keys() if i not in ['lines', 'mjd']]
        self.FilePath = self.path + self.FileName
        if not os.path.exists(self.FilePath):
            self.download()
        self.read_table()

    def download(self):
        print(f'Downloading {self.URL}...')
        urlretrieve(self.URL, self.FilePath)

    def __extract(self, line, i1, i2):
        tmp = line[i1-1:i2]
        if tmp.strip().replace('.','').replace('-','').isdigit():
            return float(tmp)
        else:
            np.nan

    def __read1(self, data):
        # https://maia.usno.navy.mil/ser7/readme.finals2000A
        data = [i for i in data if len(i.strip())>20]
        flag_A = []
        mjd = []
        px_A = []
        py_A = []
        ut1_utc_A = []
        dx_A = []
        dy_A = []
        px_B = []
        py_B = []
        ut1_utc_B = []
        dx_B = []
        dy_B = []
        for i in data:
            mjd.append(self.__extract(i, 7, 12))
            px_A.append(self.__extract(i, 19, 27))
            py_A.append(self.__extract(i, 38, 46))
            ut1_utc_A.append(self.__extract(i, 59, 68))
            dx_A.append(self.__extract(i, 98, 106))
            dy_A.append(self.__extract(i, 117, 125))
            px_B.append(self.__extract(i, 135, 144))
            py_B.append(self.__extract(i, 145, 154))
            ut1_utc_B.append(self.__extract(i, 155, 165))
            dx_B.append(self.__extract(i, 166, 175))
            dy_B.append(self.__extract(i, 176, 185))

        dc = {
            'mjd':mjd,
            'px_A':px_A, 'py_A':py_A, 'ut1_utc_A':ut1_utc_A, 'dx_A':dx_A, 'dy_A':dy_A,
            'px_B':px_B, 'py_B':py_B, 'ut1_utc_B':ut1_utc_B, 'dx_B':dx_B, 'dy_B':dy_B,
            }
        return dc

    def __read234(self, data):
        dc = {}
        data = data[self.__trim['lines']:]
        data = [i for i in data if len(i)>0]
        dc['mjd'] = [float(i[self.__trim['mjd'][0]:self.__trim['mjd'][1]]) for i in data]
        for c in self.columns:
            dc[c] = [float(i[self.__trim[c][0]:self.__trim[c][1]]) for i in data]
        return dc

    def read_table(self):
        with open(self.FilePath, 'r') as f:
            data = f.read().split('\n')
        if self.kind == 1:
            dc = self.__read1(data)
            df = pd.DataFrame(dc)#.astype(float)
        else:
            dc = self.__read234(data)
            df = pd.DataFrame(dc).astype(float)
        self.table = df
    
    def interpolate(self, mjd):
        if self.table is None:
            self.read_table()
        df = self.table
        if 'px_A' in df.columns:
            if np.isnan(df[df['mjd']>=mjd].iloc[0]['px_B']): # use Bul.A
                df = df[[i for i in df.columns if i[-2:]!='_B']]
                self.bulletin = 'A'
            else: # use Bul.B
                df = df[[i for i in df.columns if i[-2:]!='_A']]
                self.bulletin = 'B'
            df.columns = ['mjd', 'px', 'py', 'ut1_utc', 'dx', 'dy']
            
        if (mjd < df['mjd'].iloc[0]) or (mjd > df['mjd'].iloc[-1]):
            raise Exception('MJD out of range!')
        dc = {}
        for c in df.columns:
            if c!='mjd':
                dc[c] = np.interp(mjd, df['mjd'], df[c])
        return dc

    def get_eop(self, t):
        """
        Calculates the interpolated Earth orientation parameters

        Argument:
            t : datetime, jd, or str
        Returns:
            dc : dictionary of parameters
        """
        if isinstance(t, datetime):
            mjd = dt_to_mjd(t)
        elif (isinstance(t, float)) or (isinstance(t, int)):
            mjd = t - 2400000.5
        elif isinstance(t, str):
            mjd = dt_to_mjd(iso2dt(t))

        return self.interpolate(mjd)

