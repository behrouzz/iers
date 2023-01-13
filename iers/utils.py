"""
Module utils
------------
"""

def is_data(row):
    isdata = False
    numbers = sum(i.isdigit() for i in row)
    letters = sum(i.isalpha() for i in row)
    #spaces  = sum(i.isspace() for i in row)
    if (len(row)>1) and (letters==0):
        #print(numbers/len(row))
        if (numbers/len(row)) > 0.3:
            isdata = True
            
    return isdata


def extract(file):
    with open(file, 'r') as f:
        raw = f.read()
    rawlist = raw.split('\n')
    data = []
    for row in rawlist:
        if is_data(row):
            rowlist = row.split(' ')
            rowlist = [float(i) for i in rowlist if len(i)>0]
            data.append(rowlist)
    return raw, data

