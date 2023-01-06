col_bc_lps = ['MJD', 'day', 'month', 'year', 'TAI-UTC']

col_psi_eps =[ #Psi,Eps
    'MJD','PM-X','PM-Y','UT1-TAI',
    'DPSI','DEPS',#PPP
    'X-ERR','Y-ERR','UT1-ERR',
    'DPSI-ERR','DEPS-ERR', #PPP
    'RMS DELAY','CORR X-Y','CORR X-U','CORR Y-U',
    'CORR DP-DE', #ppp
    'IND1','IND2','IND3','XRT','YRT','LOD',
    'DPSIRT','DEPSRT', #PPP
    'XRT-ERR','YRT-ERR','LOD-ERR',
    'DPSIRT-ERR','DEPSRT-ERR' # PPP
    ]


col_x_y = [ #x,y
    'MJD','PM-X','PM-Y','UT1-TAI',
    'DX','DY', #ppp
    'X-ERR','Y-ERR','UT1-ERR',
    'DX-ERR','DY-ERR', #ppp
    'RMS DELAY','CORR X-Y','CORR X-U','CORR Y-U',
    'CORR DX-DY', #ppp
    'IND1','IND2','IND3','XRT','YRT','LOD',
    'DXRT','DYRT', # ppp
    'XRT-ERR','YRT-ERR','LOD-ERR',
    'DXRT-ERR','DYRT-ERR' #
    ]

col_psi_eps_brief = [
    'an','x','x_er','y','y_er','UT1-TAI','UT1_er',
    'dPsi','dPsi_er','dEps','dEps_er' #ppp
    ]

col_x_y_brief = [
    'an','x','x_er','y','y_er','UT1-TAI','UT1_er',
    'dX','dX_er','dY','dY_er' # ppp
    ]

col_psi_eps_brief_02 = [
    'year','month','day','mjd','x','y','UT1-UTC','LOD',
    'dPsi','dEps',
    'x_er','y_er','UT1-UTC_er','LOD_err',
    'dPsi_er','dEps_er'
    ]

col_x_y_brief_02 = [
    'year','month','day','mjd','x','y','UT1-UTC','LOD',
    'dX','dY',
    'x_er','y_er','UT1-UTC_er','LOD_err',
    'dX_er','dY_er'
    ]


col_x_y_03 = [
    'year','month','day','hour','mjd','x','y','UT1-UTC',
    'dX','dY','xrt','yrt','LOD',
    'x_er','y_er','UT1-UTC_er','dX_er','dY_er',
    'xrt_er','yrt_er','LOD_er'
    ]

col_psi_eps_03 = [
    'year','month','day','hour','mjd','x','y','UT1-UTC',
    'dPsi','dEps','xrt','yrt','LOD',
    'x_er','y_er','UT1-UTC_er','dPsi_er','dEps_er',
    'xrt_er','yrt_er','LOD_er'
    ]


files_dc = {
    
    'Leap_Second.dat': {# delete year,month,day
        'adr': 'bul/bulc/',
        'cols': col_bc_lps,
        'int': [2,3,4,5],
        },

    # EOP
    'eopc01.1846-now': {
        'adr': 'eop/eopc01/',
        'cols': col_psi_eps,
        'int': [17,18,19],
        },

    'eopc01.1900-now.dat': {
        'adr': 'eop/eopc01/',
        'cols': col_psi_eps_brief,
        'int': [],
        },

    'eopc01.iau2000.1846-now': {
        'adr': 'eop/eopc01/',
        'cols': col_x_y,
        'int': [17,18,19],
        },

    'eopc01.iau2000.1900-now.dat': {
        'adr': 'eop/eopc01/',
        'cols': col_x_y_brief,
        'int': [],
        },
    
    'filtered-pole.tab': { #1900-2023
        'adr': 'eop/eopc01/',
        'cols': ['year', 'xf', 'yf'],
        'int': [],
        },
    
    'mean-pole.tab': { #1900-2016
        'adr': 'eop/eopc01/',
        'cols': ['year', 'xm', 'ym'],
        'int': [],
        },

    'eopc04.62-now': {
        'adr': 'eop/eopc04/',
        'cols': col_psi_eps_brief_02,
        'int': [1,2,3],
        },

    'eopc04.dPsi_dEps.12h.84-now': {
        'adr': 'eop/eopc04/',
        'cols': col_psi_eps_brief_02[:3]+['hour']+col_psi_eps_brief_02[3:],
        'int': [1,2,3,4],
        },

    'eopc04.dPsi_dEps.62-now': {
        'adr': 'eop/eopc04/',
        'cols': col_psi_eps_brief_02,
        'int': [1,2,3],
        },

    'eopc04.dX_dY.12h.84-now': {
        'adr': 'eop/eopc04/',
        'cols': col_x_y_brief_02[:3]+['hour']+col_x_y_brief_02[3:],
        'int': [1,2,3,4],
        },

    'eopc04_IAU2000.62-now': {
        'adr': 'eop/eopc04/',
        'cols': col_x_y_brief_02,
        'int': [],
        },

    'eopc04.12h.1984-now': {
        'adr': 'eop/eopc04_20/',
        'cols': col_x_y_03,
        'int': [1,2,3,4],
        },

    'eopc04.1962-now': {
        'adr': 'eop/eopc04_20/',
        'cols': col_x_y_03,
        'int': [1,2,3,4],
        },

    'eopc04.dPsi_dEps.12h.1984-now': {
        'adr': 'eop/eopc04_20/',
        'cols': col_psi_eps_03,
        'int': [1,2,3,4],
        },

    'eopc04.dPsi_dEps.1962-now': {
        'adr': 'eop/eopc04_20/',
        'cols': col_psi_eps_03,
        'int': [],
        },

    # SERIES
    'bkg_r.eop': {
        'adr': 'series/operational/',
        'cols': col_psi_eps[:3] + ['UT1-UTC'] + col_psi_eps[4:],
        'int': [17,18,19],
        },
    
    'eopc02.1830-now': {
        'adr': 'series/longterm/',
        'cols': col_psi_eps,
        'int': [17,18,19],
        },

    'hmnao_a_2021.eop': {
        'adr': 'series/longterm/',
        'cols': col_psi_eps,
        'int': [17,18,19],
        },

    'eopc04_extended.dat': {
        'adr': 'series/prediction/',
        'cols': col_x_y_brief_02,
        'int': [1,2,3],
        },

    'eopc04R35d_IAU2000_daily': {
        'adr': 'series/opa/',
        'cols': col_x_y_brief_02,
        'int': [1,2,3],
        },
    
    'eopc04R35d_IAU2000': {
        'adr': 'series/opa/',
        'cols': col_x_y_brief_02,
        'int': [1,2,3],
        },


    }





