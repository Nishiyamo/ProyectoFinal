from datetime import datetime
from sqlalchemy.sql.expression import and_
from DataStatsStockExchange.SQLAlchemy.Connector import Securities_Historico

# Nombre valor (TSL), ADJ_CLOSE, DATE to graphic
class StockDataSets:

    @staticmethod
    def get_adj_close(symbol, start_date, end_date):
        from DataStatsStockExchange.application.app import db
        parsed_start_date = datetime.fromisoformat(start_date)
        parsed_end_date = datetime.fromisoformat(end_date)

        list = db.session.query(Securities_Historico).filter(
            and_(
                Securities_Historico.symbol == symbol,
                Securities_Historico.date >= parsed_start_date,
                Securities_Historico.date <= parsed_end_date
            )
        ).all()


        labels = [element.date.strftime(format='%Y/%m/%d') for element in list]
        dataset = [element.adj_close for element in list]


        return {
            'labels': labels,
            'dataset': dataset
        }
