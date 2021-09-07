import os
import pandas as pd
import numpy as np


def get_list_tickers(directory):    
    files = os.listdir(directory)
    tickers = [i.split('.csv')[0] for i in files]
    
    return tickers 


def profit_factor(result):
    sumpol = result[result > 0].sum()
    sumotr = result[result < 0].sum()
    if sumotr != 0: return sumpol / abs(sumotr)
    elif sumotr == 0 and sumpol != 0: return 999
    elif sumotr == 0 and sumpol == 0: return 0


def rsi_indicator(close, rsi_period):
    series = close
    delta = series.diff().dropna()
    u = delta * 0
    d = u.copy()
    u[delta > 0] = delta[delta > 0]
    d[delta < 0] = -delta[delta < 0]
    u[u.index[rsi_period-1]] = np.mean( u[:rsi_period] ) #first value is sum of avg gains
    u = u.drop(u.index[:(rsi_period-1)])
    d[d.index[rsi_period-1]] = np.mean( d[:rsi_period] ) #first value is sum of avg losses
    d = d.drop(d.index[:(rsi_period-1)])
    rs = pd.DataFrame.ewm(u, com=rsi_period-1, adjust=False).mean() / \
            pd.DataFrame.ewm(d, com=rsi_period-1, adjust=False).mean()
    rsi = 100 - 100 / (1 + rs)
    
    return rsi


def sharp(df):
    df['Pcnt_change'] = df['Account'].pct_change()
    df.fillna(0, inplace=True)

    df_return = (df['Pcnt_change'] * 252).mean()
    df_vola = df['Pcnt_change'].std() * (252**(0.5))
    df_sharpe = df_return/df_vola 

    return df_sharpe.round(2)


def max_dd(df_nav):
    high = df_nav.cummax()
    dd = (1 + high) / (1 + df_nav) - 1
    max_dd = max(dd) * 100

    return round(max_dd, 2)


def test_func():
    return 'Test is done'



