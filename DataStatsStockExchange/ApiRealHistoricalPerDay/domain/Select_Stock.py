from DataStatsStockExchange.ApiRealHistoricalPerDay.domain.ConnectionDB import con
import json

def select_url_stock_exchange(con):
    curs = con.cursor()
    sql_sentence = "select url, symbol from stocks_exchange"
    curs.execute(sql_sentence)
    records = curs.fetchall()

    urls_symbols = []
    for row in records:
        urls_symbols.append({'url': row[0], 'symbol': row[1]})

    records_stocks_url = json.dumps(urls_symbols)
    return records_stocks_url
    # print(records_stocks_url)

# select_url_stock_exchange(con())