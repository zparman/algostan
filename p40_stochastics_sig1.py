#!/usr/bin/python3
# p40
# Generate signal for stochastic crossover
# if previous stochastic K-line is < stochastic D-line
#    and current K-line > D-line
# then 
#     get Date and Symb
#     get_returns 

import os
import sys
import pandas as pd
import talib

# Global Variables
DATADIR = 'data/ta/'
DATBDIR = 'data/pnl/'
WORKDIR = 'data/tickers/'
OUTFDIR = 'data/signal/'
BASKET = 'tick1'
BASKET = 'sp500'
BASKET = 'tick5'
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
        df_ta   = pd.read_csv(DATADIR+symb+YNN)
        df_pnl  = pd.read_csv(DATBDIR+symb+'_alldates'+YNN)
        df_stochastic_sig1  = get_stochastic_sig1(symb,df_ta)


# Get list of tickers for a given basket
def get_tickers(basket):
    tickers = pd.read_csv(SYMBFILE)
    return tickers

# Get technical indicators
def get_stochastic_sig1(s,df0):
    outfile = OUTFDIR+s+'_stoch_sig1.csv'+YNN
    sys.stdout = open(outfile,'w')
    df2 = pd.DataFrame()
    # loop
    for i in range(1,len(df0)):
        curr = i
        prev = i -1
        if  (   (df0.at[prev,'stokk'] <= df0.at[prev,'stokd'])  
            and (df0.at[curr,'stokk'] >  df0.at[curr,'stokd']) 
            and (df0.at[prev,'stokk'] <= 20) 
            and (df0.at[curr,'stokk'] >  20)
            ):
                d = df0.at[curr,'Date']
                print(s,d)      
    sys.stdout.close()
    return(df2)



    

def init():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

def fini():
    exit()

if __name__ == '__main__':
    main()
