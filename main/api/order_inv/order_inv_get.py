from flask import make_response, jsonify

from main.models import Order_inv
from main.common import sha_required

from main.api.order_inv import api


@api.route("/order-inv/")
@sha_required
def order_inv_get():
	orders = Order_inv.query.all()
	data = [order.to_json() for order in orders]

	res = {
		"data": data
	}

	return make_response(jsonify(res))