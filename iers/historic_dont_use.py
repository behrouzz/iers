from .core import EOP
from .time import mjd_to_dt
import numpy as np
import pandas as pd

"""
MJD
---
kind 1 is UTC
kind 2 is UTC
kind 3 is UT1
kind 4 is UT1
"""


def add_t(df):
    df = df.copy()
    for c in df.columns:
        if ('x' in c) or ('y' in c) or ('o' in c):
            del df[c]
    if ('ut1_tai' in df.columns) and (df['mjd'].iloc[0]==-4703.268): #kind=3
        df = df.loc[df['ut1_tai'].notnull()]
    df['t'] = df['mjd'].apply(lambda x: mjd_to_dt(x))
    return df

def kind(mjd):
    k1i = 41684.0
    k2i, k2f = 37665.0, 60525.0
    k3i, k3f = 35473.352, 60547.215
    k4i, k4f = -1409424.00, 57387.87
    k = 99
    if mjd > k1i:
        k = 1
    elif mjd > k2i:
        k = 2
    elif mjd > k3i:
        k = 3
    elif mjd > k4i:
        k = 4
    return k

def add_kind(df):
    df = df.copy()
    df['k'] = df['mjd'].apply(lambda x: kind(x))
    return df


def get_all():
    e1 = EOP(1)
    e2 = EOP(2)
    e3 = EOP(3)
    e4 = EOP(4)

    df1 = add_t(e1.table)
    df2 = add_t(e2.table)
    df3 = add_t(e3.table)
    df4 = add_t(e4.table)

    df1 = add_kind(df1)
    df2 = add_kind(df2)
    df3 = add_kind(df3)
    df4 = add_kind(df4)

    df2 = df2[df2['k']>=2]
    df3 = df3[df3['k']>=3]
    df4 = df4[df4['k']>=4]

    # k1 bul A or B
    df1['ut1_utc'] = np.nan
    df1.loc[df1['ut1_utc_B'].notnull(), 'ut1_utc'] = df1['ut1_utc_B']
    df1.loc[df1['ut1_utc_B'].isnull(), 'ut1_utc'] = df1.loc[df1['ut1_utc_B'].isnull(), 'ut1_utc_A']
    df1 = df1[list(df2.columns)]

    # remove shared lines
    if df4['mjd'].iloc[-1]==df3['mjd'].iloc[0]:
        df4 = df4[df4['mjd']!=df4['mjd'].iloc[-1]]
    if df3['mjd'].iloc[-1]==df2['mjd'].iloc[0]:
        df3 = df3[df3['mjd']!=df3['mjd'].iloc[-1]]
    if df2['mjd'].iloc[-1]==df1['mjd'].iloc[0]:
        df2 = df2[df2['mjd']!=df2['mjd'].iloc[-1]]

    # concat
    df1['k'] = 1
    df2['k'] = 2
    df21 = pd.concat([df2, df1], axis=0)
    df21['d_type'] = 'ut1_utc'
    df21.columns = ['mjd', 'delta', 't', 'k', 'd_type']

    df3['k'] = 3
    df4['k'] = 4
    df43 = pd.concat([df4, df3], axis=0)
    df43['d_type'] = 'ut1_tai'
    df43.columns = ['mjd', 'delta', 't', 'k', 'd_type']

    df = pd.concat([df43, df21], axis=0, ignore_index=True)
    return df
