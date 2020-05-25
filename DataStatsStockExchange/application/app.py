from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from DataStatsStockExchange.application.api import GetDataApi, GetSecuritieApi, GetStockExchange

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:bunta@localhost:3306/stocksdb'
app.config['SQLAQLCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app)
api = Api(app)
api.add_resource(GetDataApi, '/data/')
api.add_resource(GetSecuritieApi, '/securitie/')
api.add_resource(GetStockExchange, '/')
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run()

