**Author:** [Behrouz Safari](https://behrouzz.github.io/)<br/>
**License:** [MIT](https://opensource.org/licenses/MIT)<br/>

# iers
*Analysis data of the International Earth Rotation and Reference Systems Service (IERS)*


## Installation

Install the latest version of *iers* from [PyPI](https://pypi.org/project/iers/):

    pip install iers

Requirements are *numpy* and *pandas* and will be installed automatically if needed.


## Quick start

Let's get parameters for the *Julian Date* 2460556.5 and print the results.

```python
from iers import EOP
dc = EOP().get_eop(2460556.5)
print(dc)
```

Output:

```
{'px': 0.211611, 'py': 0.44424, 'ut1_utc': 0.0531643, 'dx': 0.349, 'dy': 0.088}
```

## More

Currently, this package can retrieve Earth Orientation Parameters from four files. It should be indicated with *kind* argument of EOP class. The first kind, which is default, gets daily data from 1973-01-02 until a few month after current date. The second kind is daily data from 1962-01-01 until a few days before the current date. The third kind is from 1846 until now, but its is not daily. It is 0.1 year interval (from 1846 from 1889) and 0.05 year interval (from 1890 to now). The fourth kind is longterm historical table from 2000 B.C. until 2015.

You should create an instance of the *EOP* class by passing the kind of table you want to `kind` argument. Then you can get the table with 'table' attribute.

```python
from iers import EOP

eop = EOP(kind=1)
print(eop.table)
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

Let's use another *kind*:


```python
from iers import EOP

eop = EOP(kind=2)
print(eop.table)
```

Output:

```
           mjd        px        py   ut1_utc       lod        dx        dy
0      37665.0 -0.012700  0.213000  0.032634  0.001723  0.000000  0.000000
1      37666.0 -0.015900  0.214100  0.032055  0.001669  0.000000  0.000000
2      37667.0 -0.019000  0.215200  0.031553  0.001582  0.000000  0.000000
3      37668.0 -0.021999  0.216301  0.031144  0.001496  0.000000  0.000000
4      37669.0 -0.024799  0.217301  0.030815  0.001416  0.000000  0.000000
...        ...       ...       ...       ...       ...       ...       ...
22856  60521.0  0.157404  0.478195  0.023001 -0.000948  0.000321 -0.000074
22857  60522.0  0.159281  0.477650  0.024048 -0.001134  0.000357 -0.000077
22858  60523.0  0.161188  0.477331  0.025258 -0.001283  0.000402 -0.000092
22859  60524.0  0.163634  0.476656  0.026573 -0.001325  0.000448 -0.000106
22860  60525.0  0.166545  0.476250  0.027893 -0.001291  0.000413 -0.000105
```

You can get the available parameters for a desired moment by passing the time as *datetime* or *Julian Date* or *string* to the `.get_eop()` method. If the *kind* is 1, it will use bulletin *B* if there is available data, otherwise uses bulletin *A*. You can check which bulletin has been used for interpolation with `bulletin` attribute.

```python
from iers import EOP

eop = EOP(kind=1)

dc = eop.get_eop('2024-05-02 21:37:50')

print(dc)
print('Bulletin used:', eop.bulletin)
```

Output:

```
{'px': 0.0069811804398159285, 'py': 0.40801708148148286, 'ut1_utc': -0.01803119438657428, 'dx': 0.2808885416666599, 'dy': -0.16251909722223354}
Bulletin used: B
```

The files will be downloaded automatically and saved in *Documents* folder of user, so the next time you do not need to download the file again. Any file that is older than 7 days, will be downloaded automatically. By the way, if you want newer versions of a file, you can use the `.download()` method to download it again.

```python
from iers import EOP

eop = EOP(kind=1)
eop.download()
```

## Leap Seconds

To get leap seconds for a given time, pass the time as *datetime* or *Julian Date* or *string* to the `leap_seconds` function.

```python
from iers import leap_seconds

r = leap_seconds('2012-01-15 15:40:33')
print(r)
```

Output:

```
34
```

See more at [https://behrouzz.github.io/astrodatascience/](https://behrouzz.github.io/astrodatascience/)
