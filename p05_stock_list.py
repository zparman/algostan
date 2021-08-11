#!/usr/bin/python3
# p05_stock_list.py
# Get stock list for SP500 from wikipedia.

import numpy as np
import pandas as pd
WORKDIR = 'data/tickers/'
BASKET = 'sp500'
ticker_file = WORKDIR+BASKET+'_tickers.csv'

# url of sp500 companies from wikipedia
html_tables = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

# the first html table has the list of companies
df = html_tables[0]

# save the wikipedia list
df.to_csv(WORKDIR+BASKET+'_wikipedia.csv')

# drop some tickers
df = df[df['Symbol'] != 'BRK.B']
df = df[df['Symbol'] != 'BF.B']

# save just the symbols, no index
df.to_csv(ticker_file, columns=['Symbol'],index=False)

# read csv_file
df1 = pd.read_csv(ticker_file,)
print(ticker_file)
print(df1)
exit(0)

'''
# List symbols
symbols = df['Symbol'].values.tolist()
for symbol in symbols:
    print(symbol)
    exit(0)
'''    
