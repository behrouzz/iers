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

eop = EOP(kind=1)
df = eop.read_table()
```

Output:

```
           mjd      px_A      py_A  ut1_utc_A  ...   py_B  ut1_utc_B    dx_B   dy_B
0      41684.0  0.120733  0.136966   0.808418  ...  0.137     0.8075 -18.637 -3.667
1      41685.0  0.118980  0.135656   0.805616  ...  0.134     0.8044 -18.636 -3.571
2      41686.0  0.117227  0.134348   0.802790  ...  0.131     0.8012 -18.669 -3.621
3      41687.0  0.115473  0.133044   0.799873  ...  0.128     0.7981 -18.751 -3.769
4      41688.0  0.113717  0.131746   0.796814  ...  0.126     0.7949 -18.868 -3.868
...        ...       ...       ...        ...  ...    ...        ...     ...    ...
19236  60920.0  0.179201  0.355850   0.104524  ...    NaN        NaN     NaN    NaN
19237  60921.0  0.179305  0.355138   0.105691  ...    NaN        NaN     NaN    NaN
19238  60922.0  0.179391  0.354423   0.106704  ...    NaN        NaN     NaN    NaN
19239  60923.0  0.179458  0.353706   0.107474  ...    NaN        NaN     NaN    NaN
19240  60924.0  0.179507  0.352987   0.107948  ...    NaN        NaN     NaN    NaN

[19241 rows x 11 columns]
```

Or, with another *kind*:


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

You can get the available parameters for a desired moment by passing the time as Modified Julian Date to the *mjd* parameter of *.interpolate()* method. If the *kind* is 1, it will use bulletin *B* if there is available data, otherwise uses bulletin *A*. You can check which bulletin has been used for interpolation with *.bulletin* attribute.

```python
from iers import EOP

eop = EOP(kind=1)

dc = eop.interpolate(mjd=41685.5)

print(dc)
print('Bulletin used:', eop.bulletin)
```

Output:

```
{'px': 0.14, 'py': 0.1325, 'ut1_utc': 0.8028, 'dx': -18.6525, 'dy': -3.596}
Bulletin used: B
```

The files will be downloaded automatically and saved on *Documents* folder of the user, so the next time you do not need to download the file again. But if you want newer versions of a file after a while, you can use the *.download()* method to download it again.

```python
from iers import EOP

eop = EOP(kind=1)
eop.download()
```

See more at [https://behrouzz.github.io/astrodatascience/](https://behrouzz.github.io/astrodatascience/)
