import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api


JWT_KEY = os.getenv('JWT_SECRET', 'ISURU')

app = Flask(__name__, static_folder=None)
app.config['API_TITLE'] = 'Product Service'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'
app.debug = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.sqlite"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)
