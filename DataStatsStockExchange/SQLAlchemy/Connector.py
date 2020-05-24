from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Table, Float, Date
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:bunta@localhost:3306/stocksdb'
app.config['SQLAQLCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Base = declarative_base()

# class schema():
#     Table('securities')

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