from flask import request
from flask_restful import Resource, fields, marshal_with

from DataStatsStockExchange.domain.repo import StockDataSets

securitie_marshaller = {
    'name': fields.String,
    'symbol': fields.String,
}

class GetDataApi(Resource):
    def get(self):

        params = request.args

        symbol = params.get('symbol')
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        return StockDataSets.get_adj_close(symbol, start_date, end_date)


class GetSecuritieApi(Resource):
    @marshal_with(securitie_marshaller)
    def get(self):

        params = request.args

        stock = params.get('stock')

        return StockDataSets.get_securities_basics(stock)


