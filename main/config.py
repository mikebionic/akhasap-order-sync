import os
import sys
import json

# app_config = os.environ.get('USERPROFILE') + '\\barcodeapp\\config.json'

if sys.platform.startswith('win'):
	app_config = f"{os.getcwd()}\\config.json"
else:
	app_config = f"{os.getcwd()}/config.json"

main_config = None

if os.path.exists(app_config) and os.path.isfile(app_config):
	config_path = app_config
	with open(config_path) as fp:
		main_config = json.load(fp)

class Config:
	FLASK_ENV = main_config["FLASK_ENV"] if main_config else 'development'
	TESTING = main_config["TESTING"] if main_config else 1
	DEBUG = main_config["DEBUG"] if main_config else 1
	SECRET_KEY = main_config["SECRET_KEY"] if main_config else "asdlfkhyueflbawkueyfhklaskdvjfsnadIUGxee3r"
	# SQLALCHEMY_DATABASE_URI = main_config["SQLALCHEMY_DATABASE_URI"] if main_config else 'postgresql://postgres:123456@localhost:5432/dbSapHasap'
	# SQLALCHEMY_DATABASE_URI = main_config["SQLALCHEMY_DATABASE_URI"] if main_config else 'sqlite:///accounting.db'
	SQLALCHEMY_DATABASE_URI = main_config["SQLALCHEMY_DATABASE_URI"] if main_config else 'mssql+pyodbc://sa:123456@127.0.0.1:1433/akhasap_db?driver=ODBC+Driver+17+for+SQL+Server?TrustedConnection=yes'