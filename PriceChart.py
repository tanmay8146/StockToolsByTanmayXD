#modules
import math
import pandas_datareader as web 
import numpy as np
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
from os import system

from sympy import Min

plt.style.use('fivethirtyeight')

system('clear')

asset= input("ENTER STOCK / CRYPTOCURRENCY SYMBOL\nFOR BITCOIN, WRITE 'BTC': ")
startDate = input("ENTER STARTING DATE IN YYYY-MM-DD FORMAT: ")
endDate = input("ENTER ENDING DATE IN YYYY-MM-MM FORMAT: ")

    #get the stock quote
df = web.DataReader('%s'%asset, data_source= 'yahoo', start= '%s'%startDate, end= '%s'%endDate)
print(df)

    #saving data frame to a file
df.to_csv('%sDataFrame.csv'%asset)

    #visualize the closing price                plot 01
plt.figure(figsize=(16,8))
plt.title('%s Price closing history by TanmayXD'%asset)
plt.plot(df['Close'])
plt.xlabel('Date', fontsize= 18)
plt.ylabel('Close Price USD ($)', fontsize= 18)
plt.show()

    #Get the number of rows and columns in the data set
print(df.shape)

    #Create a data frame with only 'Close' column
data = df.filter(['Close'])
        # Convert the data frame to a numpy array
dataset= data.values
        #Get the number of rows to train the model
training_data_len = math.ceil(len(dataset) * .8)

print(training_data_len)

        #scale the data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)
print(scaled_data)