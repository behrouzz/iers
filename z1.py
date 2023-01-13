from datetime import datetime
from iers.time import ut1_to_era, era_to_ut1, jd_to_dt
import numpy as np

d2r = np.pi/180
r2d = 180/np.pi

# For now, suppose that t is in UT1
t = datetime.now()
#t = datetime(1958, 1, 1)
print(t)

era = ut1_to_era(t, date_time=True, degree=True)
print(era, ' ==%360==> ', era%360)

ut1 = era_to_ut1(era, date_time=True, degree=True)
print(ut1)

dt = (ut1-t).total_seconds() * 1_000_000
print(f'-> Difference: {dt} microseconds')
