import numpy as np
from datetime import datetime, timedelta
from iers.tempp import get_historic

#dut1_array, pm_x1, pm_y1 = get_finals2000a('finals2000A.txt')
mjd, pm_x, pm_y, ut1_tai = get_historic()
