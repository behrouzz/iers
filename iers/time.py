"""
Module time
-----------
Time conversions


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

d2r = np.pi/180
r2d = 180/np.pi

#====================================================
# JULIAN DATE
#====================================================

def dt_to_mjd(t):
    t0 = datetime(1858, 11, 17, 0)
    return (t - t0).total_seconds()/86400


def mjd_to_dt(mjd):
    t0 = datetime(1858, 11, 17, 0)
    try:
        dt = t0 + timedelta(days=mjd)
    except:
        dt = jd_to_datetime(mjd + 2400000.5)
    return dt


def dt_to_jd(t):
    t0 = datetime(1858, 11, 17, 0)
    mjd = (t - t0).total_seconds()/86400
    jd = mjd + 2400000.5
    if t < datetime(1582,10,15):
        jd += 10
    return jd


def jd_to_dt(jd):
    if jd < 2299160.5:
        jd -= 10
    mjd = jd - 2400000.5
    t0 = datetime(1858, 11, 17, 0)
    dt = t0 + timedelta(days=mjd)
    return dt


def jd_to_datetime(jd):

    jd = jd + 0.5
    F, I = math.modf(jd)
    I = int(I)
    A = math.trunc((I - 1867216.25)/36524.25)
    
    if I > 2299160:
        B = I + 1 + A - math.trunc(A / 4.)
    else:
        B = I
        
    C = B + 1524
    D = math.trunc((C - 122.1) / 365.25)
    E = math.trunc(365.25 * D)
    G = math.trunc((C - E) / 30.6001)
    day = C - E + F - math.trunc(30.6001 * G)
    
    if G < 13.5:
        month = G - 1
    else:
        month = G - 13
        
    if month > 2.5:
        year = D - 4716
    else:
        year = D - 4715

    d_ = day
    d = int(d_)
    h_ = (d_-d)*24
    h = int(h_)
    m_ = (h_-h)*60
    m = int(m_)
    s_ = (m_-m)*60
    s = int(s_)
    ms_ = (s_-s)*1000000
    ms = int(ms_)

    try:
        dt = datetime(year, month, d, h, m, s, ms)
    except:
        dt = (year, month, d, h, m, s, ms)
        
    return dt

#====================================================
# ERA
#====================================================

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


#====================================================
# Time Scales
#====================================================

def ut_to_tai(t):
    pass

def tai_to_ut(t):
    pass
