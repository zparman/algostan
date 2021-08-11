#!/usr/bin/python3
import os
import pandas as pd
# Rank stock list based on 3 day price and volume.

BASKET = 'sp500'
DATADIR = 'data/yfinance/'       # data files
WORKDIR = 'data/tickers/'       # work path
OUTFDIR = 'data/pv/'     # output files
YNN = '_y2y.csv'
SYMBFILE = WORKDIR+BASKET+'_tickers.csv'

tickers = pd.read_csv(SYMBFILE)

# Get last date from aapl
aapl = pd.read_csv(DATADIR+'AAPL'+YNN)

# Loop through dates
for i in range(len(aapl)-1, len(aapl)-10 , -1):
#for i in range(0,len(aapl)-1, 1):
    curr_date = (aapl.loc[i, 'Date'])
    print(i, curr_date)

  # Output file
    SYMBFIL2 = OUTFDIR+BASKET+'_'+curr_date+'.csv'
    for ticker in range(0, len(tickers)):
        symb = tickers.iloc[ticker]['Symbol']
        symbfile = (DATADIR+symb+YNN)
        df = pd.read_csv(symbfile)
        df['pv'] = df['Close'] * df['Volume']
        df['symb'] = symb
        df_filtered = df[(df.Date == curr_date)]
        df2 = pd.DataFrame(df_filtered[['Date', 'symb', 'pv','Close']])
        if (ticker == 0):
            df2.to_csv(SYMBFIL2, index=False, header=True, mode='w')
        else:
            df2.to_csv(SYMBFIL2, index=False, header=None, mode='a')

    # Read file of all symbols for the current date
    df = pd.read_csv(SYMBFIL2)
    df.sort_values(by=['pv'], inplace=True, ascending=False, ignore_index=True)
    df.drop(['pv'], axis=1)
    df.round(0)
    df.to_csv(SYMBFIL2, mode='w')
    print(SYMBFIL2)
    # print(df.head(5))
    # print(df.tail(5))

exit()

