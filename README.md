# Finance econometrics

Finance econometrics and helpful function

## Instructions

1. Install

```
pip install finance_econometrics
```

2. Import 

``` 
from finance_econometrics import *
```

3. Use functions

### get_list_tickers

```
# parameter of function - link to directory with files (AA.csv, AAPL.csv)
import os
DIRECTORY = '/home/user/data/us_equities/'
TICKERS = get_data(DIRECTORY)
# got list of tickers ['AA', 'AAPL']
```

### profit_factor

```
# parameter of function - Series with all deals (not NAV)
profit_fact = round(profit_factor(df_all_deals['result_deal']), 2)
# got value of profit factor 5.30

```

### rsi_indicator

```
import pandas as pd
import numpy as np
RSI_PERIOD = 13
df['RSI'] = rsi_indicator(df['Close'], RSI_PERIOD)
# got column of values in DataFrame
```

### sharp

```
# parameter of function - Series NAV
# in DataFrame must need column with name Account
df = pd.read_csv('df_nav_result.csv')
sharp_value = sharp(df)
# got value of sharp 0.98
```

### max_dd

```
# parameter of function - Series NAV
df_nav = df['Account']
max_dd = max_dd(df_nav)
# got value of max drawdown 12.47
```
