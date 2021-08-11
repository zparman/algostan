#!/usr/bin/python3
# p31_ta_indicator.py

import pandas as pd
import talib

# Global Variables
DATADIR = 'data/yfinance/'
WORKDIR = 'data/tickers/'
OUTFDIR = 'data/ta/'
BASKET = 'tick5'
BASKET = 'sp500'
SYMBFILE = WORKDIR+BASKET+'_tickers.csv'
YNN = '_y2y.csv'



def main():
    print("main")
    init()
    basket = BASKET
    tickers = get_tickers(basket)

    # loop through each ticker
    for i, row in tickers.iterrows():
        symb           = (row['Symbol'])
        # Skip these symbols
        if symb == 'BRK.B' or symb == 'BF.B':
            continue
        print(symb)
        df_yfinance    = pd.read_csv(DATADIR+symb+YNN)
        df_tindicators = get_tindicators(symb, df_yfinance)


# Get list of tickers for a given basket
def get_tickers(basket):
    tickers = pd.read_csv(SYMBFILE)
    return tickers

# Get technical indicators
def get_tindicators(s,df0):
    # df0                    # input dataframe
    df1 = pd.DataFrame()     # output dataframe

    df1['Date'] = df0['Date']
    df1['sma20'] = talib.SMA(df0['Close'], timeperiod=20)
    df1['sma50'] = talib.SMA(df0['Close'], timeperiod=50)
    df1['bbu'], df1['bbm'], df1['bbl'] = talib.BBANDS(df0['Close'],
        timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    df1['macd'], df1['macds'], df1['macdh'] = talib.MACD(df0['Close'],
        fastperiod=12, slowperiod=26, signalperiod=9)
    df1['stokk'], df1['stokd'] = talib.STOCH(df0['High'], df0['Low'], df0['Close'],
        fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    df1['rsi'] = talib.RSI(df0['Close'], timeperiod=14)
    df1['willr'] = talib.WILLR(df0['High'], df0['Low'], df0['Close'], timeperiod=14)

    df2 = df1.dropna()
    df2.to_csv(OUTFDIR+s+YNN)
    print(df2)
    return df2

def init():
    print("initialization")

def fini():
    print("finalization")

if __name__ == '__main__':
    main()



