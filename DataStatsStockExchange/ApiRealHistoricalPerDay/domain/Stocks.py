import mysql.connector
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import pandas as pd
from datetime import datetime, timedelta
import json
from bs4 import BeautifulSoup
import requests
import pandas as pd

import time



DEFAULT_START_DATE = '2010-01-01'
DEFAULT_END_DATE = str((datetime.today() - timedelta(-1)).strftime('%Y-%m-%d'))

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()        
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print ('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result    
    return timed

class Stocks:

    def __init__(self, db_con, start_date, end_date):

        self.load_all_data(db_con, start_date, end_date)

    def clean_data(self, stock_data, col):
        weekdays = pd.date_range(start=DEFAULT_START_DATE, end=DEFAULT_END_DATE)
        clean_data = stock_data[col].reindex(weekdays)
        return clean_data.fillna(method='ffill')

    @timeit
    def load_all_data(self, db_con, start_date=DEFAULT_START_DATE, end_date=DEFAULT_END_DATE):
        self.load_securities(db_con)

        self.data = dict()

        for stock in self.stocks:
            all_stock_securities = []

            for securitie in stock.get('stock_securities'):
                ticker = securitie.get('symbol')
                try:
                    stock_data = data.DataReader(ticker,data_source='yahoo', start=start_date, end=end_date)

                    all_stock_securities.append({"name": securitie.get("name"), "symbol": securitie.get("symbol"), "data": stock_data})
                    
                except RemoteDataError:
                    print("No hay datos para {st}".format(st=securitie.get("symbol")))

            self.data[stock.get("stock_symbol")] = all_stock_securities

    
    def load_securities(self, db_con):
        self.load_urls(db_con)

        stock_list = []

        for stock_url in self.stock_urls:
            page = requests.get(stock_url.get("url"))
            soup = BeautifulSoup(page.content, 'html.parser')

            # Scanner of html to take heads from symbols
            st = soup.find_all('a', class_='C($c-fuji-blue-1-b) Cur(p) Td(n) Fw(500)')
            symbols = list()

            count = 0
            # Extraction of all the symbols of the list()
            for i in st:
                if count < 30:
                    symbols.append(i.text)
                else:
                    break
                count +=1

            # Scanner of html to take head for names
            nt = soup.find_all('td', class_='Py(10px) Ta(start) Pend(10px)')
            names = list()

            count = 0
            # Extraction of all the full names of the list()
            for i in nt:
                if count < 30:
                    names.append(i.text)
                else:
                    break
                count +=1

            stock_list.append(
                {
                    'stock_name': stock_url.get('name'), 
                    'stock_symbol': stock_url.get('symbol'), 
                    'stock_securities': [{'symbol': symbols, 'name': names} for symbols, names in zip(symbols, names)]
                }
            )
        
        self.stocks = stock_list

    def load_urls(self, db_con):

        con = mysql.connector.connect(**db_con)

        curs = con.cursor()
        sql_sentence = "select url, symbol, name from stocks_exchange"
        curs.execute(sql_sentence)
        records = curs.fetchall()
        con.close()

        stock_urls = []
        for row in records:
            stock_urls.append({'url': row[0], 'symbol': row[1], 'name': row[2]})

        self.stock_urls = stock_urls


    def print_data(self):

        for key, data in self.data:
            print("SYMBOL: %s" % key)
            print("NAME: %s" % data.name)
            print("DATA: %s" % data.data)

    def get_single_securitie(self, securitie_symbol):

        return self.data[securitie_symbol]

    def get_prop(self, securitie_symbol, prop):

        return self.data[securitie_symbol].data[prop]
