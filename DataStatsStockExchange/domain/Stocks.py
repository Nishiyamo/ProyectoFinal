from datetime import datetime
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import json
from DataStatsStockExchange.SQLAlchemy.Connector import Securitie, db, Securities_Historico, Select_Origin


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

    def __init__(self, start_date, end_date, from_local=False):
        if from_local:
            self.load_from_local()
        else:
            self.load_all_data(start_date, end_date)

    def clean_data(self, stock_data, col):
        weekdays = pd.date_range(start=self.start_date, end=self.end_date)
        clean_data = stock_data[col].reindex(weekdays)
        return clean_data.fillna(method='ffill')

    @timeit
    def load_from_local(self):
        with open('data.json', 'r') as f:
            self.data = json.load(f)

    @timeit
    def load_all_data(self, start_date, end_date):
        self.load_securities()

        self.data = dict()

        for stock in self.stocks:
            all_stock_securities = []

            for securitie in stock.get('stock_securities'):
                ticker = securitie.get('symbol')
                try:
                    stock_data = data.DataReader(ticker, data_source='yahoo', start=start_date, end=end_date)
                    stock_data = json.loads(stock_data.reset_index().to_json(None, orient='records', date_format='iso'))
                    all_stock_securities.append({"name": securitie.get("name"), "symbol": securitie.get("symbol"), "data": stock_data})
                    
                except (IOError, RemoteDataError, KeyError):
                    print("No hay datos para {st}".format(st=securitie.get("symbol")))

            self.data[stock.get("stock_symbol")] = all_stock_securities

    def load_securities(self):
        self.load_urls()

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
                if count < 60:
                    if count % 2 != 0:
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

    def load_urls(self):
        records = db.session.query(Select_Origin).all()

        stock_urls = []
        for row in records:
            stock_urls.append({'url': row.url, 'symbol': row.symbol, 'name': row.name})

        self.stock_urls = stock_urls

    def save_to_local_data(self):
        with open('data.json', 'w') as f:
            json.dump(self.data, f, ensure_ascii=False)

    def save_data(self):
        for stock_key, stocks in self.data.items():
            for securitie in stocks:
                sec = Securitie(stock=stock_key, name=securitie.get('name'), symbol=securitie.get('symbol'))
                db.session.add(sec)
                db.session.commit()
                print("Inserted securitie: " + sec.__repr__())

                # To bulk insert, best know as bloq insertion, bd improvement
                sec_data = [
                    Securities_Historico(symbol=securitie.get('symbol'), adj_close=data.get('Adj Close'),
                                         date=datetime.fromisoformat(data.get('Date')[0:10]))
                    for data in securitie.get('data')
                ]

                db.session.bulk_save_objects(sec_data)
                db.session.commit()

    def get_single_securitie(self, securitie_symbol):

        return self.data[securitie_symbol]

    def get_prop(self, securitie_symbol, prop):

        return self.data[securitie_symbol].data[prop]
