from test import Stocks

db_config=dict(
        host='127.0.0.1',
        database='stocksdb',
        user='root',
        password='bunta'
    )

my_stock = Stocks(db_config)

my_stock.print_data()
