#!/usr/bin/python3
# p10_data.py
import pandas as pd
from datetime import datetime, timedelta, date, time
import yfinance

# Global Variables
BASKET = 'sp500'
# BASKET = 'tick1'   # one stock
DATADIR = 'data/yfinance/'
WORKDIR = 'work/'
WORKPATH = 'data/tickers/'
BASKET = 'sp500'
SYMBFILE = WORKPATH+BASKET+'_tickers.csv'
YNN = '_y2y.csv'
TGT_PCT = 105
TGT_DAYS = 20
TGT_PRICE = 0
INV_SIZE = 1000


def main():
    basket = BASKET
    tickers = get_tickers(basket)
    for i, row in tickers.iterrows():
        symb = (row['Symbol'])
        data = download_data(i, symb)
        print(data.tail())


def get_tickers(basket):
    # df = pd.read_csv(WORKDIR+'ticker'+BASKET+'pv.csv')
    df = pd.read_csv(SYMBFILE)

    return df


def download_data(pvrank, symb):
    symb_file = (DATADIR+symb+YNN)
    print(pvrank, symb_file)

    if YNN == '_y2x.csv':
        sta_date = '2000-01-01'
        end_date = '2021-01-01'
    elif YNN == '_y2y.csv':
        sta_date = '2000-01-01'
        end_date = '2022-01-01'
    elif YNN == '_y21.csv':
        sta_date = '2020-01-01'
        end_date = '2022-01-01'
    elif YNN == '_ytd.csv':
        sta_date = date.today() - timedelta(days=365)  # +1 year
        end_date = date.today() + timedelta(days=1)
    else:
        print('Invalid YNN', YNN)
        exit(0)

    df = yfinance.download(symb, sta_date, end_date, progress=False)
    df = df.round(2)                            # round numbers to 2 decimal
    df.to_csv(symb_file)
    return df


if __name__ == '__main__':
    main()

