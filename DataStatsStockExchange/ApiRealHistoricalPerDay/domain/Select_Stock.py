from DataStatsStockExchange.ApiRealHistoricalPerDay.domain.ConnectionDB import con

def select_url_stock_exchange(con):
    db = con
    curs = con.cursor()
    sql_sentence = "select url from stocks_exchange"
    curs.execute(sql_sentence)
    record = curs.fetchall()
    print(record)

select_url_stock_exchange(con())