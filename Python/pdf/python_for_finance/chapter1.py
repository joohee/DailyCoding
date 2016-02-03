import numpy as np
import pandas as pd
#import pandas.io.data as web
from pandas_datareader import data, wb

def example1():
    S0 = 100    # initial index level
    K = 105     # strike price
    T = 1.0     # time-to-maturity
    r = 0.05    # riskless short rate
    sigma = 0.2 # volatility

    I = 100000  # number of simulations

    # Valuation Algorithm
    z = np.random.standard_normal(I)        # pseudorandom nnumbers
    ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
    # index valus at maturity
    hT = np.maximum(ST - K, 0)              # inner values at maturity
    C0 = np.exp(-r * T) * np.sum(hT) / I    # Monte Carlo estimator

    # Result Output
    print("Value of the European Call option {0:5.3f}".format(C0))

def example2():
    goog = data.DataReader('GOOG', data_source='google', start='3/14/2009', end='4/14/2014')
    goog.tail()

if __name__ == "__main__":
    #example1()
    example2()
