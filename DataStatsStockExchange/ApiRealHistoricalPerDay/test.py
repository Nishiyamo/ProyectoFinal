from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

days_to_subtract = 1
START_DATE = '2005-01-01'
END_DATE = str((datetime.today() - timedelta(days_to_subtract)).strftime('%Y-%m-%d'))

# print(END_DATE)

UK_STOCK = 'AUTO:LN' #FTSE 100
USA_STOCK = 'AMZN' #NASDAQ
SP_STOCK = 'ANA.MC' #IBEX 35

def get_stats(stock_data):
    return{
        'last': np.mean(stock_data.tail(1)),
        'shot_mean': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(200)),
        'short_rolling': stock_data.rolling(window=20).mean(),
        'long_rolling': stock_data.rolling(window=200).mean()
    }

def clean_data(stock_data, col):
    weekdays = pd.date_range(start = START_DATE, end = END_DATE)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker,'yahoo',START_DATE, END_DATE)
        adj_close = clean_data(stock_data, 'Adj Close')
        
        print(adj_close)

    except RemoteDataError:
        print("No hay datos para {st}".format(st=ticker))

get_data(UK_STOCK)