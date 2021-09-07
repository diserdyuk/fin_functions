# finance econometrics

Finance econometrics and helpful function

## Instructions

1. Install

```
pip install finance_econometrics
```

```python 
from finance_econometrics import *


                     




all_functions


get_list_tickers

передается путь к директории с файлами (AA.csv, AAPL.csv)
> import os
> DIRECTORY = '/home/ds/us_data/us_all_equities_updated/'
> TICKERS = get_data(DIRECTORY)
< ['AA', 'AAPL']


profit_factor

в функцию передается Series со всеми сделками (не nav)
> profit_fact = round(profit_factor(df_all_deals['Result_deal']), 2)
< 5.30


rsi_indicator

> import pandas as pd
> import numpy as np
> RSI_PERIOD = 13
> df['RSI'] = rsi_indicator(df['Close'], RSI_PERIOD)
< получаем колонку значений индикатора


sharp

> передается Series nav
> в data frame должна быть колонка с именем Account
> df = pd.read_csv('df_nav_result.csv')
> sharp_value = sharp(df)
< 0.98


max_dd

> передается Series nav
> df_nav = df['Account']
> max_dd = max_dd(df_nav)
< 12.47



