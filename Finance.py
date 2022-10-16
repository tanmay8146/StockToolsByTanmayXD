import pandas_datareader.data as web
import math

from sklearn.preprocessing import MinMaxScaler

class finance:
    def __init__(self, asset, start_date, end_date):
        self.asset = asset
        self.startDate = start_date
        self.endDate = end_date

    def scaledData(self):
        df = web.DataReader('%s'%self.asset, data_source= 'yahoo', start= '%s'%self.startDate, end='%s'%self.endDate)
        df.to_csv('%sDataFrame.csv'%self.asset)

        data = df.filter(['Close'])
        dataset = data.values

        global training_data_len
        training_data_len = math.ceil(len(dataset) * .8)
        
        global scaled_data, scaler
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(dataset)

    def trainData(self):
        train_data = scaled_data[0:training_data_len, :]

        global x_train, y_train
        x_train = []
        y_train = []

        for i in range(60, len(train_data)):
            x_train.append(train_data[i-60:i, 0])
            y_train.append(train_data[i, 0])

            if i<= 60:
                print(x_train)
                print()
                print(y_train)
                print("x_train, y_train created for i=%s!"%i)



if __name__ == "__main__":
    details = finance(asset= 'INFY', start_date='2019-01-01', end_date='2021-01-01')
    finance.scaledData(details)
    finance.trainData(details)
    
