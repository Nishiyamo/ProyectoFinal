from DataStatsStockExchange.domain.Stocks import Stocks
import argparse
from datetime import datetime, timedelta

db_config = dict(
    host='127.0.0.1',
    database='stocksdb',
    user='root',
    password='bunta'
)

def start_stocks(start_date, end_date):
    my_stock = Stocks(db_config, start_date, end_date)
    my_stock.print_data()


def load_stocks():
    my_stock = Stocks(db_config)

if __name__ == "__main__":
    # return with "-h" the help of the args
    parser = argparse.ArgumentParser()
    # Argument to start date
    parser.add_argument("-s", "--start_date", help="Start date", default='2010-01-01')
    # Argument to end date
    parser.add_argument("-e", "--end_date", help="End date", default=str((datetime.today() - timedelta(-1)).strftime('%Y-%m-%d')))

    args = parser.parse_args()

    start_stocks(args.start_date, args.end_date)
