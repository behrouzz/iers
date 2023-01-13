"""
Module time
-----------
                                                 ET 1960-1983
                                                TDT 1984-2000
 UTC 1972-               TAI 1958-               TT 2001-
----+-----------------------+-------------------------+-----
    |                       |                         |
    |<------ TAI-UTC ------>|<-----   TT-TAI    ----->|
    |                       |      32.184s fixed      |
    |                       |                         |
    |                       |                         |
    |                                                 |
    <> delta-UT = UT1-UTC                             |
     | (max 0.9 sec)                                  |
-----+------------------------------------------------+-----
     |<-------------- delta-T = TT-UT1 -------------->|
    UT1                                            TT/TDT/ET
"""

import numpy as np
from datetime import datetime, timedelta
import math
#import csv
#import os.path
#from urllib.request import urlretrieve
from .formats import files_dc
from .core import create_df

d2r = np.pi/180
r2d = 180/np.pi

BASE = 'https://hpiers.obspm.fr/iers/'
LOCAL = 'C:/Moi/_py/Astronomy/Earth/IERS/data/'


def get_era(ut1):
    Tu = dt_to_jd(ut1) - 2451545
    ERA = 2*np.pi * (0.7790572732640 + 1.00273781191135448 * Tu)
    return 


def get_historic():
    base = LOCAL # for now
    filename = 'hmnao_a_2021.eop'
    file = base + files_dc[filename]['adr'] + filename
    df = create_df(file)
    mjd = df['MJD'].values
    pm_x = df['PM-X'].values
    pm_y = df['PM-Y'].values
    ut1_tai = df['UT1-TAI'].values
    return mjd, pm_x, pm_y, ut1_tai

"""
def get_finals2000a(file):
    with open(file, 'r') as f:
        data = f.read().split('\n')

    data = [i for i in data if len(i.strip())>68]
    mjd = [int(i[7:12]) for i in data]
    dut1 = [float(i[58:68]) for i in data]
    pm_x = [float(i[18:27]) for i in data]
    pm_y = [float(i[37:46]) for i in data]

    dut1_array = np.array(list(zip(mjd,dut1)))
    pm_x = np.array(list(zip(mjd, pm_x)))
    pm_y = np.array(list(zip(mjd, pm_y)))
    return dut1_array, pm_x, pm_y
"""
