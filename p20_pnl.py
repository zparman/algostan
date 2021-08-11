#!/usr/bin/python3
# p11_pnl.py
import sys
import numpy as np
import pandas as pd

# Global Variables
DATADIR = 'data/yfinance/'
OUTFDIR = 'data/pnl/'
WORKDIR = 'work/'
BASKET = 'tick5'
BASKET = 'sp500'
#BASKET = 'tick5'
SYMBFILE = WORKDIR+BASKET+'_tickers.csv'
YNN = '_y2y.csv'

def main():
    init()
    basket = BASKET
    tickers = get_tickers(basket)
    
    for i, row in tickers.iterrows():
        symb = (row['Symbol'])
        df_histq  = pd.read_csv(DATADIR+symb+YNN)
        # df_returns = get_results(symb, 1.05, 5, df_histq)
        df1 = df_histq.drop(['Open','Low','Adj Close','Volume'],axis=1)
        df2 = get_results_range(symb, df1)
    fini()

def init():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    sys.stdout = open(WORKDIR+'p11_results.csv','w')
    
def fini():
    #sys.stdout.close()
    exit()


def get_tickers(basket):
    tickers = pd.read_csv(SYMBFILE)
    return tickers

def get_results_range(s,df):
    df['Symb'] = s
    for x in range(3,16):
        days = x
        strdays = str(x).zfill(2)    # left pand with zero 
        tgt_pct = 100 + x
        df['MaxHi'] = df['High'].rolling(window=days, min_periods=1).max().shift(-days)
        df['ClosX'] = df['Close'].shift(-days)
        df['PctHiX'] = df['MaxHi']/df['Close'] * 100
        df['PctClX'] = df['Close'].shift(-days)/df['Close'] * 100
        df['ResultX'] = np.where(df['PctHiX'] > tgt_pct, df['Close'] * tgt_pct / 100, df['ClosX'])
        df['PctNetX'] = df['ResultX']/df['Close'] * 100
        df['PctNetX'+strdays] = df['PctNetX']
    df.drop(['High','Close', 'MaxHi','ClosX','PctHiX','PctClX','ResultX','PctNetX'],axis=1,inplace=True)    
    df.dropna(inplace=True)
    df2 = df.copy()
    #print(df2.head(15))
    #print(df2.tail(15))
    csv_file= OUTFDIR+s+'_alldates'+YNN
    df2.to_csv(csv_file)   
    #print(csv_file)
    #print(df2.iloc[:,2:].mean())
    return(df2)
'''
def get_results(s, pct, days, df):
    df['symb'] = s
    df['Hi05d'] = df['High'].rolling(window=days, min_periods=1).max().shift(-days)
    df['Cl05d'] = df['Close'].shift(-days)
    df['PctHi05'] = df['Hi05d']/df['Close'] *100
    df['PctCl05'] = df['Close'].shift(-days)/df['Close'] * 100
    df['resul05'] = np.where(df['PctHi05'] > 105, df['Close'] * 1.05, df['Cl05d'])  
    df['PctNet05'] = df['resul05']/df['Close']*100
    header = ['symb', 'Date','PctNet05']
    df.to_csv(DATADIR+s+'_PctNet05'+YNN, columns = header)   
    #print(df[['symb', 'Date', 'Close', 'Hi05d', 'Cl05d', 'PctHi05',  'PctCl05', 'resul05','PctNet05']].head(20))
    #print(df[['symb', 'Date', 'Close', 'Hi05d', 'Cl05d', 'PctHi05',  'PctCl05', 'resul05','PctNet05']].tail(20))
    #print(s, '\t', '{:.2f}'.format(round(df['PctNet05'].mean(),2)))
    return 
'''


if __name__ == '__main__':
    main()

