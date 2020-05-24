from datetime import datetime

from flask_restful import fields
from sqlalchemy.sql.expression import and_
from DataStatsStockExchange.SQLAlchemy.Connector import Securities_Historico, Securitie


# Nombre valor (TSL), ADJ_CLOSE, DATE to graphic
class StockDataSets:

    @staticmethod
    def get_adj_close(symbol, start_date, end_date):
        from DataStatsStockExchange.application.app import db
        query = db.session.query(Securities_Historico).filter(Securities_Historico.symbol == symbol)

        if start_date:
            query = query.filter(Securities_Historico.date >= start_date)

        if end_date:
            query = query.filter(Securities_Historico.date <= end_date)

        records = query.all()

        labels = [element.date.strftime(format='%Y/%m/%d') for element in records]
        dataset = [element.adj_close for element in records]


        return {
            'labels': labels,
            'dataset': dataset
        }

    @staticmethod
    def get_securities_basics(stock):
        from DataStatsStockExchange.application.app import db
        query = db.session.query(Securitie)

        if stock:
            query = query.filter(Securitie.stock == stock)

        records = query.all()

        return records