##from datetime import datetime
##import numpy as np
##import matplotlib.pyplot as plt
##import os
##from urllib.request import urlretrieve
import pandas as pd
from .utils import files_dc

def __extract(file):
    with open(file, 'r') as f:
        raw = f.read()
    rawlist = raw.split('\n')
    data = []
    for row in rawlist:
        if len(row)>0:
            if row[0]!='#':
                rowlist = row.split(' ')
                rowlist = [float(i) for i in rowlist if len(i)>0]
                data.append(rowlist)
    return raw, data


def create_df(file, first_col=None, int_cols=None):
    """
    Create DataFrame from a text file

    Arguments:
    ----------
        file      : path of file to open
        first_col : first column of data; (for trying to extract column names)
        int_cols  : columns whose data type are integer (1-based numbers)

    Returns:
    --------
        dataframe
    """
    raw, data = __extract(file)
    columns = None
    
    if file.split('/')[-1] in files_dc.keys():
        file = file.split('/')[-1]
        if len(files_dc[file]['cols']) > 0:
            columns = files_dc[file]['cols']
        if len(files_dc[file]['int']) > 0:
            int_cols = files_dc[file]['int']
    if first_col is not None:
        i1 = raw.find(first_col)
        i2 = raw.find('\n', i1)
        columns = raw[i1:i2].split(' ')
        columns = [i for i in columns if len(i)>0]

    if (columns is not None) and (len(data[0])!=len(columns)):
        columns = None
    
    df = pd.DataFrame(data, columns=columns)
    if int_cols is not None:
        int_col_names = []
        for i in int_cols:
            int_col_names.append(list(df.columns)[i-1])
        df[int_col_names] = df[int_col_names].astype(int)
    return df


def serop_to_df(file):
    """series/operational to DataFrame"""
    return create_df(file, first_col='MJD', int_cols=[17,18,19])


