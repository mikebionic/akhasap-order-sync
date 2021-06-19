# -*- coding: utf-8 -*-
from datetime import datetime

from main import db
from main.models import (
	Order_inv_line,
	Resource,
	Unit,
)

from .add_Order_inv_line_dict import add_Order_inv_line_dict


def save_order_line_synch_data(
	req,
	OInvId,
):

	data, fails, data_models = [], [], []
	this_unit = Unit.query.first()

	for order_inv_line_req in req:
		order_inv_line_data = add_Order_inv_line_dict(order_inv_line_req)
		order_inv_line_data['OInvId'] = OInvId

		ResRegNo = order_inv_line_req['ResRegNo']
		ResGuid = order_inv_line_req['ResGuid']

		this_line_resource = Resource.query\
			.filter_by(
				ResRegNo = ResRegNo,
				ResGuid = ResGuid,
				GCRecord = None)\
			.first()

		try:
			if not this_line_resource:
				print(f"order has no resource by guid {ResGuid} and reg no {ResRegNo}")
				raise Exception
			order_inv_line_data["ResId"] = this_line_resource.ResId
			order_inv_line_data["UnitId"] = this_unit.UnitId

			OInvLineRegNo = order_inv_line_data['OInvLineRegNo']
			OInvLineGuid = order_inv_line_data['OInvLineGuid']

			thisOrderInvLine = Order_inv_line.query\
				.filter_by(
					OInvLineGuid = OInvLineGuid,
					# OInvLineRegNo = OInvLineRegNo,
					GCRecord = None)\
				.first()

			if thisOrderInvLine:
				order_inv_line_data["OInvLineId"] = thisOrderInvLine.OInvLineId
				thisOrderInvLine.update(**order_inv_line_data)
				data.append(order_inv_line_req)

			else:
				thisOrderInvLine = Order_inv_line(**order_inv_line_data)
				db.session.add(thisOrderInvLine)
				data.append(order_inv_line_req)
				thisOrderInvLine = None
			
			data_models.append(thisOrderInvLine)

		except Exception as ex:
			print(f"{datetime.now()} | OInv Api OInvLine Exception: {ex}")
			fails.append(order_inv_line_req)

	if fails:
		for model in data_models:
			db.session.expunge(model)

	return data, fails