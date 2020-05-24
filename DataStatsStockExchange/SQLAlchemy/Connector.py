from sqlalchemy import Column, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#OBJ Securitie
class Securitie(Base):
    __tablename__ = 'securities'

    name = Column(String(200))
    symbol = Column(String(10), primary_key=True)
    stock = Column(String(10))

    def __init__(self, name, symbol, stock):
        self.name = name
        self.symbol = symbol
        self.stock = stock

    def __repr__(self):
        return "<Securities(name='%s', symbol='%s', stock='%s')>" % (self.name, self.symbol, self.stock)

#OBJ Securitie_Historica
class Securities_Historico(Base):
    __tablename__ = 'securities_historico'

    symbol = Column(String(10), primary_key=True)
    adj_close = Column(Float)
    date = Column(Date)

    def __init__(self, symbol, adj_close, date):
        self.symbol = symbol
        self.adj_close = adj_close
        self.date = date

    def __repr__(self):
        return "Securities_Historico(symbol= '%s', adj_close= '%s', date= '%s')" % (self.symbol, self.adj_close, self.date)

#URL OBJ
class Select_Origin(Base):
    __tablename__ = 'stocks_exchange'

    name = Column(String(10), primary_key=True)
    url = Column(String(200))
    symbol = Column(String(10))

    def __init__(self, name, url, symbol):
        self.name = name
        self.url = url
        self.symbol = symbol

    def __repr__(self):
        return "Select_Origin(name= '%s', url= '%s', symbol= '%s')" % (self.name, self.url, self.symbol)
