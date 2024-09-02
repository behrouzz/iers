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

def iso2dt(t_str):
    if len(t_str)!=19:
        raise Exception('Date string must be like "2024-02-10 09:30:58"')
    else:
        return datetime.strptime(t_str.replace('T', ' '), '%Y-%m-%d %H:%M:%S')


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
# Any to MJD
#====================================================

def any2mjd(t):
    if isinstance(t, datetime):
        mjd = dt_to_mjd(t)
    elif (isinstance(t, float)) or (isinstance(t, int)):
        mjd = t - 2400000.5
    elif isinstance(t, str):
        mjd = dt_to_mjd(iso2dt(t))
    else:
        raise Exception('Can not parse time')
    return mjd

#====================================================
# Leap Second
#====================================================

def leap_seconds(t):
    """
    Returns leap seconds for a given UTC time

    Argument:
        t (datetime, jd, or str): time
    Returns:
        leap seconds
    """
    mjd = any2mjd(t)    
    if mjd < 41317:
        r = 0
    else:
        mjds = [
            41317.0, 41499.0, 41683.0, 42048.0, 42413.0, 42778.0, 43144.0,
            43509.0, 43874.0, 44239.0, 44786.0, 45151.0, 45516.0, 46247.0,
            47161.0, 47892.0, 48257.0, 48804.0, 49169.0, 49534.0, 50083.0,
            50630.0, 51179.0, 53736.0, 54832.0, 56109.0, 57204.0, 57754.0
            ]
        secs = [
            10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37
            ]
        ls = [*zip(mjds, secs)]
        #ls = sorted(ls, key=lambda x: x[0])
        r = [i for i in ls if i[0]<=mjd][-1][1]
    return r

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

##def ut_to_tai(t):
##    pass
##
##def tai_to_ut(t):
##    pass


