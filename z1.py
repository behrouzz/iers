from datetime import datetime
from iers.transform import ut1_to_era, era_to_ut1
from iers.utils import jd_to_dt
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

dt = (ut1-t).microseconds
print(f'-> Difference: {dt} microseconds')

"""
The Persian
"* alf Ind"|309.3918000320833|-47.2915007225|33.17
"UCAC4 212-183274"


select main_id, ra, dec, plx_value from basic
where 
(plx_value<35)
 AND
(plx_value>31)       
AND 
CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', 309.3918000320833, -47.2915007225, 1)) = 1
"""
