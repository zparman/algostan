#!/usr/bin/python3
# t01.TA-lib.py
import numpy
import talib

def main():
    print("main")
    init()
    function_API_examples()    # Verify function API examples
    abstract_API_examples()    # Verify function API examples
    fini()
    exit(0)
    
def init():
    print("initialization")
   
def function_API_examples():
    close = numpy.random.random(100)

    # Calculate a simple moving average of the close prices:
    output = talib.SMA(close)
    print(output)

    # Calculate bollinger bands, with triple exponential average:
    from talib import MA_Type
    upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
    print(upper,middle, lower)

    # Calculate momentum of the close prices, with a time period of 5:
    output = talib.MOM(close,timeperiod=5)
    print(output)

'''
LARTODO: fix this routine

def abstract_API_examples():
    # Abstract API Quick Start

    # note that all ndarrays must be the same length!
    inputs = {
        'open': np.random.random(100),
        'high': np.random.random(100),
        'low': np.random.random(100),
        'close': np.random.random(100),
        'volume': np.random.random(100)
    }
    print(inputs)
    
    #Functions can either be imported directly or instantiated by name:
    from talib import abstract
    sma = abstract.SMA
    sma = abstract.Function('sma')
    print(sma)
     
    #From there, calling functions is basically the same as the function API:
     
    from talib.abstract import *
    output = SMA(input_arrays, timeperiod=25) # calculate on close prices by default
    output = SMA(input_arrays, timeperiod=25, price='open') # calculate on opens
    upper, middle, lower = BBANDS(input_arrays, 20, 2, 2)
    slowk, slowd = STOCH(input_arrays, 5, 3, 0, 3, 0) # uses high, low, close by default
    slowk, slowd = STOCH(input_arrays, 5, 3, 0, 3, 0, prices=['high', 'low', 'open'])
'''

def fini():
    print("finalization")

if __name__ == '__main__':
    main()


