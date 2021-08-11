#!/usr/bin/python3
# program   : p32_ta_candlestick.py
# reference : https://mrjbq7.github.io/ta-lib/func_groups/momentum_indicators.html

import pandas as pd
import talib

# Global Variables
DATADIR = 'data/yfinance/'
WORKDIR = 'data/tickers/'
OUTFDIR = 'data/cp/'
BASKET = 'tick5'
BASKET = 'sp500'
SYMBFILE = WORKDIR+BASKET+'_tickers.csv'
YNN = '_y2y.csv'



def main():
    print("main")
    init()

    # get list of tickers in the basket
    basket = BASKET
    tickers = get_tickers(basket)

    # loop through each ticker
    for i, row in tickers.iterrows():
        symb           = (row['Symbol'])
        if symb == 'BRK.B' or symb == 'BF.B':
            continue
        print(symb)
        df_yfinance    = pd.read_csv(DATADIR+symb+YNN)
        df_candlestickp = get_candlestickp(symb, df_yfinance)

# Get list of tickers for a given basket
def get_tickers(basket):
    tickers = pd.read_csv(SYMBFILE)
    return tickers

# Get candlestick pattern
def get_candlestickp(s,df0):
    # df0                    # input dataframe
    df1 = pd.DataFrame()     # output dataframe

    ### CDL2CROWS - Two Crows
    df1['c00'] = talib.CDL2CROWS(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDL3BLACKCROWS - Three Black Crows
    df1['c01'] = talib.CDL3BLACKCROWS(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDL3INSIDE - Three Inside Up/Down
    df1['c02'] = talib.CDL3INSIDE(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDL3LINESTRIKE - Three-Line Strike 
    df1['c03'] = talib.CDL3LINESTRIKE(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDL3OUTSIDE - Three Outside Up/Down
    df1['c04'] = talib.CDL3OUTSIDE(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDL3STARSINSOUTH - Three Stars In The South
    df1['c05'] = talib.CDL3STARSINSOUTH(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDL3WHITESOLDIERS - Three Advancing White Soldiers
    df1['c06'] = talib.CDL3WHITESOLDIERS(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLABANDONEDBABY - Abandoned Baby
    df1['c07'] = talib.CDLABANDONEDBABY(df0['Open'], df0['High'], df0['Low'], df0['Close'], penetration=0)
    ### CDLADVANCEBLOCK - Advance Block
    df1['c08'] = talib.CDLADVANCEBLOCK(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLBELTHOLD - Belt-hold
    df1['c09'] = talib.CDLBELTHOLD(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLBREAKAWAY - Breakaway
    df1['c10'] = talib.CDLBREAKAWAY(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLCLOSINGMARUBOZU - Closing Marubozu
    df1['c11'] = talib.CDLCLOSINGMARUBOZU(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLCONCEALBABYSWALL - Concealing Baby Swaldf0['Low']
    df1['c12'] = talib.CDLCONCEALBABYSWALL(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLCOUNTERATTACK - Counterattack
    df1['c13'] = talib.CDLCOUNTERATTACK(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLDARKCLOUDCOVER - Dark Cloud Cover
    df1['c14'] = talib.CDLDARKCLOUDCOVER(df0['Open'], df0['High'], df0['Low'], df0['Close'], penetration=0)
    ### CDLDOJI - Doji
    df1['c15'] = talib.CDLDOJI(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLDOJISTAR - Doji Star
    df1['c16'] = talib.CDLDOJISTAR(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDL7RAGONFLYDOJI - Dragonfly Doji
    df1['c18'] = talib.CDLDRAGONFLYDOJI(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLENGULFING - Engulfing Pattern
    df1['c19'] = talib.CDLENGULFING(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLEVENINGDOJISTAR - Evening Doji Star
    df1['c20'] = talib.CDLEVENINGDOJISTAR(df0['Open'], df0['High'], df0['Low'], df0['Close'], penetration=0)
    ### CDLEVENINGSTAR - Evening Star
    df1['c21'] = talib.CDLEVENINGSTAR(df0['Open'], df0['High'], df0['Low'], df0['Close'], penetration=0)
    ### CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
    df1['c22'] = talib.CDLGAPSIDESIDEWHITE(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLGRAVESTONEDOJI - Gravestone Doji
    df1['c23'] = talib.CDLGRAVESTONEDOJI(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLHAMMER - Hammer
    df1['c24'] = talib.CDLHAMMER(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLHANGINGMAN - Hanging Man
    df1['c25'] = talib.CDLHANGINGMAN(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLHARAMI - Harami Pattern
    df1['c26'] = talib.CDLHARAMI(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLHARAMICROSS - Harami Cross Pattern
    df1['c27'] = talib.CDLHARAMICROSS(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDL8IGHWAVE - High-Wave Candle
    df1['c28'] = talib.CDLHIGHWAVE(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLHIKKAKE - Hikkake Pattern
    df1['c29'] = talib.CDLHIKKAKE(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLHIKKAKEMOD - Modified Hikkake Pattern
    df1['c30'] = talib.CDLHIKKAKEMOD(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLHOMINGPIGEON - Homing Pigeon
    df1['c31'] = talib.CDLHOMINGPIGEON(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLIDENTICAL3CROWS - Identical Three Crows
    df1['c32'] = talib.CDLIDENTICAL3CROWS(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLINNECK - In-Neck Pattern
    df1['c33'] = talib.CDLINNECK(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLINVERTEDHAMMER - Inverted Hammer
    df1['c34'] = talib.CDLINVERTEDHAMMER(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLKICKING - Kicking
    df1['c35'] = talib.CDLKICKING(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
    df1['c36'] = talib.CDLKICKINGBYLENGTH(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLLADDERBOTTOM - Ladder Bottom
    df1['c37'] = talib.CDLLADDERBOTTOM(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLLONGLEGGEDDOJI - Long Legged Doji
    df1['c38'] = talib.CDLLONGLEGGEDDOJI(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLLONGLINE - Long Line Candle
    df1['c39'] = talib.CDLLONGLINE(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLMARUBOZU - Marubozu
    df1['c40'] = talib.CDLMARUBOZU(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLMATCHINGLOW - Matching Low
    df1['c41'] = talib.CDLMATCHINGLOW(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLMATHOLD - Mat Hold
    df1['c42'] = talib.CDLMATHOLD(df0['Open'], df0['High'], df0['Low'], df0['Close'], penetration=0)
    ### CDLMORNINGDOJISTAR - Morning Doji Star
    df1['c43'] = talib.CDLMORNINGDOJISTAR(df0['Open'], df0['High'], df0['Low'], df0['Close'], penetration=0)
    ### CDLMORNINGSTAR - Morning Star
    df1['c44'] = talib.CDLMORNINGSTAR(df0['Open'], df0['High'], df0['Low'], df0['Close'], penetration=0)
    ### CDLONNECK - On-Neck Pattern
    df1['c45'] = talib.CDLONNECK(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLPIERCING - Piercing Pattern
    df1['c46'] = talib.CDLPIERCING(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLRICKSHAWMAN - Rickshaw Man
    df1['c47'] = talib.CDLRICKSHAWMAN(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLRISEFALL3METHODS - Rising/Falling Three Methods
    df1['c48'] = talib.CDLRISEFALL3METHODS(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLSEPARATINGLINES - Separating Lines
    df1['c49'] = talib.CDLSEPARATINGLINES(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLSHOOTINGSTAR - Shooting Star
    df1['c50'] = talib.CDLSHOOTINGSTAR(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLSHORTLINE - Short Line Candle
    df1['c51'] = talib.CDLSHORTLINE(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLSPINNINGTOP - Spinning Top
    df1['c52'] = talib.CDLSPINNINGTOP(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLSTALLEDPATTERN - Stalled Pattern
    df1['c53'] = talib.CDLSTALLEDPATTERN(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLSTICKSANDWICH - Stick Sandwich
    df1['c54'] = talib.CDLSTICKSANDWICH(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLTAKURI - Takuri (Dragonfly Doji with very long df0['Low']er shadow)
    df1['c55'] = talib.CDLTAKURI(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLTASUKIGAP - Tasuki Gap
    df1['c56'] = talib.CDLTASUKIGAP(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLTHRUSTING - Thrusting Pattern
    df1['c57'] = talib.CDLTHRUSTING(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLTRISTAR - Tristar Pattern
    df1['c58'] = talib.CDLTRISTAR(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLUNIQUE3RIVER - Unique 3 River
    df1['c59'] = talib.CDLUNIQUE3RIVER(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
    df1['c60'] = talib.CDLUPSIDEGAP2CROWS(df0['Open'], df0['High'], df0['Low'], df0['Close'])
    ### CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
    df1['c61'] = talib.CDLXSIDEGAP3METHODS(df0['Open'], df0['High'], df0['Low'], df0['Close'])

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



