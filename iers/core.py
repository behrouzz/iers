import os
import numpy as np
import pandas as pd
from urllib.request import urlretrieve


class EOP:
    def __init__(self, kind=1):
        if kind == 4:
            self.BASE = 'https://hpiers.obspm.fr/iers/series/longterm/'
        elif kind in [1,2,3]:
            self.BASE = 'https://datacenter.iers.org/data/latestVersion/'
        else:
            raise Exception('kind must be 1, 2, 3 or 4')
        self.path = os.path.expanduser('~/Documents/')
        self.kind = kind
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

    def download(self):
        print(f'Downloading {self.URL}...')
        urlretrieve(self.URL, self.FilePath)

    def __read1(self, data):
        data = [i for i in data if len(i.strip())>70]
        mjd = []
        px = []
        py = []
        ut1_utc = []
        lod = []
        dx = []
        dy = []
        for i in data:
            mjd.append(i[7:12])
            px.append(i[18:27])
            py.append(i[37:46])
            ut1_utc.append(i[58:68])
            _lod = i[79:86]
            _lod = float(_lod) if _lod.strip().replace('.','').replace('-','').isdigit() else np.nan
            lod.append(_lod)
            _dx = i[100:106]
            _dx = float(_dx) if _dx.strip().replace('.','').replace('-','').isdigit() else np.nan
            dx.append(_dx)
            _dy = i[119:125]
            _dy = float(_dy) if _dy.strip().replace('.','').replace('-','').isdigit() else np.nan
            dy.append(_dy)
        dc = {'mjd':mjd, 'px':px, 'py':py, 'ut1_utc':ut1_utc, 'lod':lod, 'dx':dx, 'dy':dy}
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
        else:
            dc = self.__read234(data)
        df = pd.DataFrame(dc).astype(float)
        return df
    
    def interpolate(self, mjd):
        df = self.read_table()
        if (mjd < df['mjd'].iloc[0]) or (mjd > df['mjd'].iloc[-1]):
            raise Exception('MJD out of range!')
        dc = {}
        for c in df.columns:
            if c!='mjd':
                dc[c] = np.interp(mjd, df['mjd'], df[c])
        return dc
