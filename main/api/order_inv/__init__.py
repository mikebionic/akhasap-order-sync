from flask import Blueprint

api = Blueprint('order_inv_api', __name__)

from . import (
	order_inv_get,
	order_inv_post
)