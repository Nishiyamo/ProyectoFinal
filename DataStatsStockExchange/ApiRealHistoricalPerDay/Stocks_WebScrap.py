from bs4 import BeautifulSoup
import requests
import pandas as pd

# Download of the HTML that contains the first 30 stocks of FTSE100
url = 'https://es.finance.yahoo.com/quote/%5EFTSE/components?p=%5EFTSE'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Scanner of html to take the Toma de cabeceras de bolsa
st = soup.find_all('a', class_='C($c-fuji-blue-1-b) Cur(p) Td(n) Fw(500)')
symbols = list()

# Estraccion de las siglas dentro de las clases
for i in st:
    symbols.append(i.text)

# To json
js = pd.DataFrame({'Simbolo': symbols})

print(js)