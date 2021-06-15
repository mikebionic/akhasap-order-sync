from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyodbc

from main.config import Config

db = SQLAlchemy()

def create_app(config_class = Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)

	from main.api.order_inv import api as order_inv_api
	app.register_blueprint(order_inv_api)
	


	return app
