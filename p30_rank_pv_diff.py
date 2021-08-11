#!/usr/bin/python3
import os
import pandas as pd
# Rank stock list based on 3 day price and volume.


BASKET = 'sp500'              # list of stocks 
DATADIR = 'data/yfinance/'    # yahoo finance qoutes
DATBDIR = 'data/pv/'          # price volume      
DATCDIR = 'data/tickers/'       # tickers        
YNN = '_y2y.csv'
SYMBFILE = DATCDIR+BASKET+'_tickers.csv'
SYMBFIL2 = DATCDIR+BASKET+'_ranked.csv'
tickers = pd.read_csv(SYMBFILE)
SYMBFIL2 = SYMBFIL2
if os.path.exists(SYMBFIL2):
    os.remove(SYMBFIL2)

# Get list of dates
#df = pd.read_csv(DATADIR+'AAPL'+YNN)
#curr_date = (df.loc[len(df)-3, 'Date'])
#yest_date = (df.loc[len(df)-4, 'Date'])
# Get last date from aapl
aapl = pd.read_csv(DATADIR+'AAPL'+YNN)
# for i in range(len(aapl)-1, len(aapl)-99, -1):
for i in range(len(aapl)-5, len(aapl), 1):
    curr_date = (aapl.loc[i, 'Date'])
    prev_date = (aapl.loc[i-1, 'Date'])
    print("=============", i, curr_date, prev_date)
    PVFILE1 = DATBDIR+BASKET+'_'+curr_date+'.csv'
    PVFILE2 = DATBDIR+BASKET+'_'+prev_date+'.csv'

    # Diff today and yesterday's pv rank
    df1 = pd.read_csv(PVFILE1)
    df1.rename(columns={'Unnamed: 0': 'rank_x'}, inplace=True)
    # print(df1)

    df2 = pd.read_csv(PVFILE2)
    df2.rename(columns={'Unnamed: 0': 'rank_y'}, inplace=True)
    # print(df2)
    df3 = pd.merge(df1, df2, how='inner', on=['symb', 'symb'])
    df3['pv_diff'] = df3['pv_x'] - df3['pv_y']
    df3['rank_diff'] = df3['rank_y'] - df3['rank_x']
    df3['price_chg'] = (df3['Close_x'] - df3['Close_y'])/df3['Close_y']*100
    df3.sort_values(by=['pv_diff'], ascending=False, inplace=True)
    df4 = df3[(df3.price_chg > 1) & (
        df3.rank_x < df3.rank_y) & (df3.pv_diff > 0)]
    df4 = df4[['Date_x', 'symb', 'rank_x', 'rank_y',
               'price_chg', 'pv_diff', 'rank_diff']].head(10)
    print(df4.to_string(index=False, header=True))

    df3.sort_values(by=['rank_diff'], ascending=False, inplace=True)
    df4 = df3[(df3.price_chg > 1) & (
        df3.rank_x < df3.rank_y) & (df3.pv_diff > 0)]
    df4 = df4[['Date_x', 'symb', 'rank_x', 'rank_y',
               'price_chg', 'pv_diff', 'rank_diff']].head(10)
    print(df4.to_string(index=False, header=True))

    # print(df4.head(10))
    #print(df4[['Date_x', 'symb']].head(5))
    #df3.sort_values(by=['rank_diff'], ascending=False, inplace=True)
    #df4 = df3[(df3.price_chg > 1)]

    #print(df4[['Date_x', 'symb']].head(5))
    # print(df4.head(10))
    # exit()
exit()

