import json
from bs4 import BeautifulSoup
import requests
import pandas as pd
from DataStatsStockExchange.ApiRealHistoricalPerDay.domain.Select_Stock import select_url_stock_exchange
from DataStatsStockExchange.ApiRealHistoricalPerDay.domain.ConnectionDB import con

def search(one_url_stock_exchange):
    # Download of the HTML that contains the first 30 stocks of FTSE100
    url = one_url_stock_exchange
    page = requests.get(url)
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

    # To json

    js = json.dumps([{'symbol': symbols, 'name': names} for symbols, names in zip(symbols, names)])
    # print(js)
    return js

def load_one_url(string):
    urls_json = json.loads(string)
    for url in urls_json:
        search(url['url'])

# Load of the different functional methods
string = select_url_stock_exchange(con())
load_one_url(string)