"""
fortran package UAI2000.package
-------------------------------

convert the UAI 1980 celestial pole offsets (dpsi,deps)_1980
to the UAI 2000 celestial pole offsets (dpsi,desp)_2000,
(dX,dY)_2000 and conversely.

based on IERS conventions 2003 and SOFA Fortran package

Recommended subroutines :

DXDY2000_DPSIDEPS1980(dmjd,dpsi,deps,dX,dY)
DPSIDEPS1980_DXDY2000(dmjd,dX,dY,dpsi,deps)
DPSIDEPS2000_DPSIDEPS1980(dmjd,dpsi,deps,dpsi_2000,deps_2000)
DPSIDEPS2000_DXDY2000(dmjd,dX,dY,dpsi,deps)
DXDY2000_DPSIDEPS2000(dmjd,dpsi,deps,dX,dY)


dmjd       : modified julian date 
dpsi       : celestial pole offset dpsi / UAI 1980 en mas
deps       : --------------------- deps -----------------
dpsi_2000  : celestial pole offset dpsi / UAI 2000  en mas
deps_2000  : --------------------- deps ------------------
dX         : celestial pole offset dX / UAI 2000  en mas
dY         : --------------------- dY ------------------
"""

import numpy as np
#from datetime import datetime, timedelta
from .utils import jd_to_dt, dt_to_jd

d2r = np.pi/180
r2d = 180/np.pi

"""
def get_ERA(utc, dut1):
    ut1 = utc + timedelta(seconds=dut1)
    #Du = datetime_to_jd(ut1) - 2451545
    Du = dt_to_jd(ut1) - 2451545 # new
    ERA = 2*np.pi * (0.7790572732640 + 1.00273781191135448 * Du)
    era_deg = ERA * (180/np.pi)
    return era_deg % 360
"""

from hypatie import jd_to_datetime

def ut1_to_era(ut1, date_time=True, degree=True):
    if date_time:
        ut1 = dt_to_jd(ut1)
        
    Du = ut1 - 2451545
    era = 2*np.pi * (0.7790572732640 + 1.00273781191135448 * Du)
    if degree:
        era = era * r2d
    return era #% 360


def era_to_ut1(era, date_time=True, degree=True): # IRAD
    # Official definition of UT1 as a function of ERA
    if degree:
        era = era * d2r
    top = era + 2*np.pi*(1.00273781191135448*2451545-0.7790572732640)
    ut1 = top / (2*np.pi * 1.00273781191135448)
    if date_time:
        ut1 = jd_to_dt(ut1)
    return ut1
