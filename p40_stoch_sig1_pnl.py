#!/usr/bin/python3
# p40
# Generate signal for stoch crossover
# if previous stoch K-line is < stoch D-line
#    and current K-line > D-line
# then 
#     get Date and Symb

import os
import sys
import pandas as pd
import talib

# Global Variables
DATADIR = 'data/signal/'
DATBDIR = 'data/pnl/'
WORKDIR = 'data/tickers/'
#BASKET = 'tick5'
BASKET = 'sp500'
#BASKET = 'tick1'
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
        if symb == 'BRK.B' or symb == 'BF.B':
            continue
        df_sig  = pd.read_csv(DATADIR+symb+'_stoch_sig1'+YNN)
        #print(df_sig.head())
        df_pnl  = pd.read_csv(DATBDIR+symb+'_alldates'+YNN,index_col=0)
        #print(df_pnl.head())
        df_all = pd.merge(df_pnl, df_sig, on='Date')
        #df_all = df_all.dropna(inplace=True)
        df_rpt = (df_all[['Date','Symb_x','PctNetX05']])
        #print(df_rpt)
        print(df_rpt.describe())

# Get list of tickers for a given basket
def get_tickers(basket):
    tickers = pd.read_csv(SYMBFILE)
    return tickers

def init():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

def fini():
    exit()

if __name__ == '__main__':
    main()
