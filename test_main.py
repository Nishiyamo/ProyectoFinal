from DataStatsStockExchange.ApiRealHistoricalPerDay.domain.Stocks import Stocks

import argparse

db_config = dict(
    host='127.0.0.1',
    database='stocksdb',
    user='root',
    password='bunta'
)

def start_stocks(start_date, end_date):
    my_stock = Stocks(db_config, start_date, end_date)


if __name__ == "__main__":
    parser = argparse.ArgumentParser() # return with "-h" the help of the args
    parser.add_argument("-s", "--start_date", help="Start date") # Argument to start date
    parser.add_argument("-e", "--end_date", help="End date") # Argument to end date

    args = parser.parse_args()

    start_stocks(args.start_date, args.end_date)