from flask import request
from flask_restful import Resource

from DataStatsStockExchange.domain.repo import StockDataSets


class GetDataApi(Resource):
    def get(self):

        params = request.args

        symbol = params.get('symbol')
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        return StockDataSets.get_adj_close(symbol, start_date, end_date)


