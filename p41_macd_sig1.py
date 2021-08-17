#!/usr/bin/python3
# p40
# Generate signal for stoch crossover
# if previous stoch K-line is < stoch D-line
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
        df_ta   = pd.read_csv(DATADIR+symb+YNN)
        df_pnl  = pd.read_csv(DATBDIR+symb+'_alldates'+YNN)
        df_macd_sig1  = get_macd_sig1(symb,df_ta)


# Get list of tickers for a given basket
def get_tickers(basket):
    tickers = pd.read_csv(SYMBFILE)
    return tickers

# Get technical indicators
def get_macd_sig1(s,df0):
    outfile = OUTFDIR+s+'_macd_sig1'+YNN
    sys.stdout = open(outfile,'w')
    print('Date'+","+'Symb')    # dataframe column header
    df1 = pd.DataFrame
    # loop
    for i in range(1,len(df0)):
        curr = i
        prev = i -1
        if  (   (df0.at[prev,'macd'] <= df0.at[prev,'macds'])  
            and (df0.at[curr,'macd'] >  df0.at[curr,'macds']) 
            ):
                d = df0.at[curr,'Date']
                print(d+","+s)      
    sys.stdout.close()
    sys.stdout = open(outfile,'r')

    #sys.stdout = os.fdopen(1,'w',0)    # reset stdout           
    #df1 = pd.read_csv(outfile)
    #print(df1)
    return(df1)

def get_pnl(symb,date):
    infile = OUTFDIR+s+'_macd_sig1'+YNN
    df1 = read_csv(infile)
    print(infile)



    

def init():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

def fini():
    exit()

if __name__ == '__main__':
    main()
