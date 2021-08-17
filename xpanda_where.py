#!/usr/bin/python3
#################################
# explore pandas.where method
# inspired by: https://www.geeksforgeeks.org/python-pandas-df1frame-where/
#################################

# importing pandas package
import os
import pandas as pd

# define input and output csv file
workdir   = '/home/larry/pycode/algostan/'
datadir   = 'data/ta/'
outpdir   = 'data/sig/'
filequal  = '_willr1'
ynn       = '_y2y.csv'
symb      = 'AAPL'
csvfile   = workdir+datadir+symb+ynn
outfile   = workdir+datadir+symb+filequal+ynn
print(csvfile)

# read csv file
df1 = pd.read_csv(csvfile,index_col=0)

# add column from previous day
df1['willr-1'] = df1['willr'].shift(1)
print(df1)


# making boolean series 
filter1 = df1["willr"]>=-50

# making boolean series of previous day
filter2 = df1["willr"].shift(1)<-50

# filtering df1 on basis of both filters
df1.where(filter1 & filter2, inplace=True)
df1.dropna(inplace=True)                   # drop nan
df2 = pd.DataFrame(data=df1,columns=['Date','willr','willr-1'])

# display
print(df2)
print(df2.describe())
df2.to_csv(outfile)
os.system("wc "+outfile)

# 
