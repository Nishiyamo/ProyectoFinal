from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import pandas as pd
from datetime import datetime, timedelta

days_to_subtract = 1
START_DATE = '2015-01-01'
END_DATE = str((datetime.today() - timedelta(days_to_subtract)).strftime('%Y-%m-%d'))

# print(END_DATE)

UK_STOCK = 'AUTO.L' #FTSE 100 =FTSE
USA_STOCK = 'AMZN' #NASDAQ =IXIC
SP_STOCK = 'ANA.MC' #IBEX 35 =IBEX

def clean_data(stock_data, col):
    weekdays = pd.date_range(start = START_DATE, end = END_DATE)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo',START_DATE, END_DATE)
        adj_close = clean_data(stock_data, 'Adj Close')
        
        print(adj_close)

    except RemoteDataError:
        print("No hay datos para {st}".format(st=ticker))

get_data(USA_STOCK)