import pandas as pd
import pandas_datareader as web
pd.core.common.is_list_like = pd.api.types.is_list_like
import datetime as dt

pd.set_option('display.max_columns',1000,'display.width',1000)

stock = ['GLD','^DJI']
start = pd.to_datetime('2005-01-01')
end = dt.datetime.today()

df = web.DataReader(stock, 'yahoo', start, end)

location = 'E:\Windows\Escritorio\ProyectoFinal\DataStatsStockExchange\ApiRealHistoricalPerDay//test.csv'

df.to_csv(location)