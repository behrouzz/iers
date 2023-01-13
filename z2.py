# 653 BC: born of Cyaxares
# 600 BC: born of Cyrus the Great


import numpy as np
from datetime import datetime, timedelta
from iers.time import *
from iers.formats import files_dc
from iers import create_df
import matplotlib.pyplot as plt
from astropy.time import Time

mjd = -898085.20 #-600-01-08 19:12:00


d2r = np.pi/180
r2d = 180/np.pi


BASE = 'https://hpiers.obspm.fr/iers/'
local = 'C:/Moi/_py/Astronomy/Earth/IERS/data/'
filename = 'hmnao_a_2021.eop'
file = local + files_dc[filename]['adr'] + filename

df = create_df(file)

a = df[df['MJD']==mjd].iloc[0]

ut1_tai = timedelta(seconds=a['UT1-TAI'])

##fig, ax = plt.subplots()
##ax.scatter(df['MJD'], df['UT1-TAI'])
##plt.show()

"""
TAI-UT1 was approximately 0 on 1958 Jan 1.

TDT = TAI + 32.184
TT - TAI = 32.184s

TDB  =  TT  +  0.001 658s * sin(g)  +  0.000 014s * sin(2*g)
g  =  357.53_d + 0.985 600 28_d * ( JD - 245 1545.0 )
(higher order terms neglected; g = Earth's mean anomaly)


delta-T =
      ET - UT   prior to 1984
      TDT - UT  1984 - 2000
      TT - UT   from 2001 and on

delta-UT =  UT - UTC

DUT = predicted value of delta-UT, rounded to 0.1s, given in some radio
      time signals.

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

t = datetime.now()
