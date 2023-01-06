**Author:** [Behrouz Safari](https://astrodatascience.net//)<br/>
**License:** [MIT](https://opensource.org/licenses/MIT)<br/>

# iers
*Analysis data of the International Earth Rotation and Reference Systems Service (IERS)*


## Installation

Install the latest version of *iers* from [PyPI](https://pypi.org/project/iers/):

    pip install iers

Requirements are *numpy* and *pandas*.


## Examples

Let's read a file:

```python
from iers import create_df

adr = '../data/eop/eopc01/'
f = adr + 'eopc01.iau2000.1846-now'

df = create_df(f)
```

Let's open all files we have downloaded from iers server:

```python
from iers import create_df, files_dc

files = [i for i in files_dc.keys() if i[:3]!='TEM']

adrs = [files_dc[i]['adr'] for i in files]

for i, f in enumerate(files):
    df = create_df('C:/Moi/_py/Astronomy/Earth/IERS/data/'+adrs[i] + f)
    print(df)
    print(len(files_dc[f]['cols']))
    print('-'*80)
```

See more examples at [astrodatascience.net](https://astrodatascience.net/)
