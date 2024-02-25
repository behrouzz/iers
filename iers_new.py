import os
import pandas as pd
from datetime import datetime
from urllib.request import urlretrieve


def dt_to_mjd(t):
    t0 = datetime(1858, 11, 17, 0)
    return (t - t0).total_seconds()/86400


class EOP:
    def __init__(self, kind=1):
        self.path = os.path.expanduser('~/Documents/')
        self.kind = kind
        if self.kind == 1:
            self.FileName = 'finals2000A.all'
            self.URL = 'https://maia.usno.navy.mil/ser7/' + self.FileName
            self.__trim = {'lines':0, 'len': 130, 'mjd':(7,12), 'dut1':(58,68), 'px':(18,27), 'py':(37,46), 'dx':(97,106), 'dy':(116,125)}
        elif self.kind == 2:
            self.FileName = 'eopc04_IAU2000.62-now'
            self.URL = 'https://hpiers.obspm.fr/iers/eop/eopc04/' + self.FileName
            self.__trim = {'lines':10, 'len': 5, 'mjd':(14,19), 'dut1':(43,53), 'px':(21,30), 'py':(32,41), 'dx':(67,76), 'dy':(78,87)}
        elif self.kind == 3:
            self.FileName = 'eopc01.iau2000.1846-now'
            self.URL = 'https://hpiers.obspm.fr/iers/eop/eopc01/' + self.FileName
            self.__trim = {'lines':7, 'len':72, 'mjd':(0,12), 'dut1':(33,44), 'px':(13,22), 'py':(23,32), 'dx':(49,58), 'dy':(62,71)}
        elif self.kind == 4:
            self.FileName = 'nao_a.eop'
            self.URL = 'https://hpiers.obspm.fr/iers/series/longterm/' + self.FileName
            self.__trim = {'lines':7, 'len':74, 'mjd':(0,13), 'dut1':(33,48), 'px':(13,23), 'py':(23,33), 'dx':(50,60), 'dy':(63,73)}
        
        self.FilePath = self.path + self.FileName
        if not os.path.exists(self.FilePath):
            self.download()

    def download(self):
        print(f'Downloading {self.URL}...')
        urlretrieve(self.URL, self.FilePath)


    def read_table(self):
        with open(self.FilePath, 'r') as f:
            data = f.read().split('\n')
        data = [i for i in data if len(i.strip())>self.__trim['len']]
        data = data[self.__trim['lines']:]
        mjd = [float(i[self.__trim['mjd'][0]:self.__trim['mjd'][1]]) for i in data]
        dut1 = [float(i[self.__trim['dut1'][0]:self.__trim['dut1'][1]]) for i in data]
        px = [float(i[self.__trim['px'][0]:self.__trim['px'][1]]) for i in data]
        py = [float(i[self.__trim['py'][0]:self.__trim['py'][1]]) for i in data]
        dx = [float(i[self.__trim['dx'][0]:self.__trim['dx'][1]]) for i in data]
        dy = [float(i[self.__trim['dy'][0]:self.__trim['dy'][1]]) for i in data]
        if self.kind == 4:
            dc = {'mjd':mjd, 'px':px, 'py':py, 'ut1_tai':dut1, 'dPsi':dx, 'dEps':dy}
        else:
            dc = {'mjd':mjd, 'px':px, 'py':py, 'dut1':dut1, 'dx':dx, 'dy':dy}
        df = pd.DataFrame(dc)
        return df

e = EOP(kind=4)
df = e.read_table()
print(df)
