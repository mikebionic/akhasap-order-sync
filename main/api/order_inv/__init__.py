from flask import Blueprint

api = Blueprint('order_inv_api', __name__)

from .routes import *