#modules
import datetime as dt
import math
import pandas_datareader.data as web 
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
from os import system

system('clear')
class Chart:
    def __init__(self, asset, start_date, end_date):
        self.asset = asset
        self.startDate = start_date
        self.endDate = end_date

    def closingPrice(self):
        df = web.DataReader('%s'%self.asset, data_source= 'yahoo', start= '%s'%self.startDate, end='%s'%self.endDate)
        df.to_csv('%sDataFrame.csv'%self.asset)
        plt.figure(figsize=(16,8))
        plt.title('%s Closing Price History by TanmayXD'%self.asset)
        plt.plot(df['Close'])
        plt.xlabel('Date', fontsize= 18)
        plt.ylabel('Close Price USD($)', fontsize= 18)
        plt.show()

#usage
if __name__ == "__main__":
    st = '2018-01-01'
    en = '2020-01-01'
    details = Chart(asset='USDT-USD', start_date= st, end_date= en)
    Chart.closingPrice(details)