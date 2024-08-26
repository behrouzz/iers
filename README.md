**Author:** [Behrouz Safari](https://behrouzz.github.io/astrodatascience/)<br/>
**License:** [MIT](https://opensource.org/licenses/MIT)<br/>

# iers
*Analysis data of the International Earth Rotation and Reference Systems Service (IERS)*


## Installation

Install the latest version of *iers* from [PyPI](https://pypi.org/project/iers/):

    pip install iers

Requirements are *numpy* and *pandas*.


## Quick start

Currently, this package can retrieve Earth Orientation Parameters from four files. It should be indicated with *kind* argument of EOP class. The first kind, which is default, gets daily data from 1973-01-02 until a few month after current date. The second kind is daily data from 1962-01-01 until a few days before the current date. The third kind is from 1846 until now, but its is not daily. It is 0.1 year interval (from 1846 from 1889) and 0.05 year interval (from 1890 to now). The fourth kind is longterm historical table from 2000 B.C. until 2015.

You should create an instance of the *EOP* class by passing the kind of table you want to *kind* argument. Then you can get the table with the *.read_table()* method.

```python
from iers import EOP

eop = EOP(kind=2)
df = eop.read_table()
```

Output:

```
           mjd        px        py   ut1_utc     lod     dx     dy
0      41684.0  0.120733  0.136966  0.808418  0.0000 -0.766 -0.720
1      41685.0  0.118980  0.135656  0.805616  3.5563 -0.751 -0.701
2      41686.0  0.117227  0.134348  0.802790  2.6599 -0.738 -0.662
3      41687.0  0.115473  0.133044  0.799873  3.0344 -0.732 -0.640
4      41688.0  0.113717  0.131746  0.796814  3.1276 -0.739 -0.644
...        ...       ...       ...       ...     ...    ...    ...
19229  60913.0  0.176207  0.366150  0.098621     NaN    NaN    NaN
19230  60914.0  0.176526  0.365482  0.098894     NaN    NaN    NaN
19231  60915.0  0.176827  0.364808  0.099280     NaN    NaN    NaN
19232  60916.0  0.177111  0.364128  0.099745     NaN    NaN    NaN
19233  60917.0  0.177377  0.363443  0.100414     NaN    NaN    NaN
```

You can get the available parameters for a desired moment by passing the time as Modified Julian Date to the *mjd* parameter of *.interpolate()* method.

```python
from iers import EOP

eop = EOP(kind=1)

dc = eop.interpolate(mjd=41685.5)
print(dc)
```

Output:

```
{'px': 0.1181035, 'py': 0.135002, 'ut1_utc': 0.8042028999999999, 'lod': 3.1081, 'dx': -0.7444999999999999, 'dy': -0.6815}
```

The files will be downloaded automatically and saved on *Documents* folder of the user, so the next time you do not need to download the file again. But if you want newer versions of a file after a while, you can use the *.download()* method to download it again.

```python
from iers import EOP

eop = EOP(kind=1)
eop.download()
```

See more at [https://behrouzz.github.io/astrodatascience/](https://behrouzz.github.io/astrodatascience/)
