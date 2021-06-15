from flask import make_response, jsonify

from main.models import Order_inv
from main.api.order_inv import api

@api.route("/test")
def test():
	return "bar"

@api.route("/order-inv/")
def orders():
	orders = Order_inv.query.all()
	data = [order.to_json() for order in orders]

	res = {
		"data": data
	}

	return make_response(jsonify(res))