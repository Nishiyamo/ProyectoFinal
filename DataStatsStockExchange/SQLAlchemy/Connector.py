from copy import deepcopy

from sqlalchemy import Column, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SerializableMixin(object):
    @staticmethod
    def _serialize(instance):
        newinstance = deepcopy(instance.__dict__)
        newinstance.pop('_sa_instance_state')
        return newinstance

    def serialize(self):
        return self._serialize(self)


class EqMixin(SerializableMixin):
    def _model_attrs(self, instance):
        return self._serialize(instance)

    def __eq__(self, other):
        classes_match = isinstance(other, self.__class__)
        a, b = self._model_attrs(self), self._model_attrs(other)
        attrs_match = (a == b)
        return classes_match and attrs_match

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, str(self._model_attrs(self)))

    def __str__(self):
        return self.__repr__()


#OBJ Securitie
class Securitie(EqMixin, Base):
    __tablename__ = 'securities'

    name = Column(String(200))
    symbol = Column(String(10), primary_key=True)
    stock = Column(String(10))

    def __init__(self, name, symbol, stock):
        self.name = name
        self.symbol = symbol
        self.stock = stock


#OBJ Securitie_Historica
class Securities_Historico(EqMixin, Base):
    __tablename__ = 'securities_historico'

    symbol = Column(String(10), primary_key=True)
    adj_close = Column(Float)
    date = Column(Date, primary_key=True)

    def __init__(self, symbol, adj_close, date):
        self.symbol = symbol
        self.adj_close = adj_close
        self.date = date


#URL OBJ
class Select_Origin(EqMixin, Base):
    __tablename__ = 'stocks_exchange'

    name = Column(String(10), primary_key=True)
    url = Column(String(200))
    symbol = Column(String(10))

    def __init__(self, name, url, symbol):
        self.name = name
        self.url = url
        self.symbol = symbol

