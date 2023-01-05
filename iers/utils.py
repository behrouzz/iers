bs01 = ['an','x','x_er','y','y_er','UT1-TAI','UT1_er',
        'dX',  'dX_er',  'dY',  'dY_er'  ]

bs02 = ['an','x','x_er','y','y_er','UT1-TAI','UT1_er',
        'dPsi','dPsi_er','dEps','dEps_er']


files_dc = {
    
    'eopc01.iau2000.1900-now.dat': {
        'adr':'eop/eopc01',
        'cols': bs01,
        'int':[],
        },
    
    'eopc01.1846-now': {
        'adr':'eop/eopc01',
        'cols':[],
        'int':[17, 18, 19],
        },

    'eopc01.iau2000.1846-now': {
        'adr':'eop/eopc01',
        'cols':['MJD','PM-X','PM-Y','UT1-TAI','DX','DY','X-ERR','Y-ERR',
                'UT1-ERR','DX-ERR','DY-ERR','RMS DELAY','CORR X-Y','CORR X-U',
                'CORR Y-U','CORR DX-DY','IND1','IND2','IND3','XRT','YRT',
                'LOD','DXRT','DYRT','XRT-ERR','YRT-ERR','LOD-ERR','DXRT-ERR',
                'DYRT-ERR'],
        'int':[17,18,19],
        },

    'eopc01.1900-now.dat': {
        'adr':'',
        'cols': bs02,
        'int': [],
        },

    'TEMPLATE': {
        'adr': '',
        'cols': [],
        'int': [],
        },

    }


