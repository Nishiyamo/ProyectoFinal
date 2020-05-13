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

count = 0
# Extraction of all the symbols of the list()
for i in st:
    if count < 30:
        symbols.append(i.text)
    else:
        break
    count +=1

# Scanner of html to take the Toma de cabeceras de bolsa
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
js = pd.DataFrame({'symbol': symbols,'name': names})

print(js)