from flask import make_response, jsonify, request

from main.common import sha_required

from main.api.order_inv import api
from main.api.order_inv.utils import save_order_synch_data


@api.route("/order-inv/", methods=['POST'])
@sha_required
def order_inv_post():
	req = request.get_json()
	print(req)

	res = save_order_synch_data(req)

	status_code = 201 if res["status"] > 0 else 200
	return make_response(jsonify(res), status_code)
