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

List of tickers

```
# parameter of function - link to directory with files (AA.csv, AAPL.csv)
import os
DIRECTORY = '/home/user/data/us_equities/'
TICKERS = get_list_tickers(DIRECTORY)
# got list of tickers ['AA', 'AAPL']
```

Profit factor

```
# parameter of function - Series with all deals (not NAV)
profit_fact = round(profit_factor(df_all_deals['result_deal']), 2)
# got value of profit factor 5.30

```

RSI indicator

```
import pandas as pd
import numpy as np
RSI_PERIOD = 13
df['RSI'] = rsi_indicator(df['Close'], RSI_PERIOD)
# got column of values in DataFrame
```

Sharp

```
# parameter of function - Series NAV
# in DataFrame must need column with name Account
df = pd.read_csv('df_nav_result.csv')
sharp_value = sharp(df)
# got value of sharp 0.98
```

Max drawdown

```
# parameter of function - Series NAV
df_nav = df['Account']
max_dd = max_dd(df_nav)
# got value of max drawdown 12.47
```
