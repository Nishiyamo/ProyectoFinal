from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, Table, Float
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:bunta@localhost:3600/stocksdb'
app.config['SQLAQLCHEMY_TRACK_MODIFICATIONS'] = False




engine = create_engine('mysql+pymysql://root:bunta@localhost:3600/stocksdb')

Base = declarative_base()

class schema():
    Table('securities')

class Securitie(Base):
    __tablename__ = 'securities'

    name = Column(VARCHAR, primary_key=True)
    symbol = Column(VARCHAR)
    stock = Column(VARCHAR)

    def __repr__(self):
        return "<Securities(name='%s', symbol='%s', stock='%s')>" % self.name, self.symbol, self.stock

class Securities_Historico(Base):
    __tablename__ = 'securities_historico'

    symbol = Column(VARCHAR)
    adj_close = Column(Float)