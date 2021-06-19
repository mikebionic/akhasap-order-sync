# -*- coding: utf-8 -*-
from datetime import datetime

from main import db
from main.models import (
	Order_inv,
	Warehouse,
	Division,
	User,
	Rp_acc,
	Work_period,
	Department,
	Plant,
)

from .add_Order_inv_dict import add_Order_inv_dict
from main.api.order_inv.utils.save_order_line_synch_data import save_order_line_synch_data



def save_order_synch_data(payload):

	req = payload["data"]

	try:
		order_invoice_data = add_Order_inv_dict(req)

		if not req["Order_inv_lines"]:
			raise Exception
		
		order_inv_lines_req = req['Order_inv_lines']
		order_invoice_data["fich_total_unit_amount"] = len(order_inv_lines_req)

		DivGuid = req['DivGuid']
		WhGuid = req['WhGuid']
		RpAccGuid = req['RpAccGuid']
		UGuid = req['UGuid']

		this_user = User.query.filter_by(UGuid = UGuid).first()
		this_rp_acc = Rp_acc.query.filter_by(RpAccGuid = RpAccGuid).first()
		this_division = Division.query.filter_by(DivGuid = DivGuid).first()
		this_warehouse = Warehouse.query.filter_by(WhGuid = WhGuid).first()

		if not this_rp_acc or not this_division or not this_warehouse:
			print(f"{this_rp_acc}, {this_division}, {this_warehouse}")
			raise Exception
		
		order_invoice_data["DivId"] = this_division.DivId
		order_invoice_data["UId"] = this_user.UId
		order_invoice_data["RpAccId"] = this_rp_acc.RpAccId
		order_invoice_data["WhId"] = this_warehouse.WhId

		this_work_period = Work_period.query.first()
		order_invoice_data["WpId"] = this_work_period.WpId

		this_department = Department.query.first()
		order_invoice_data["DeptId"] = this_department.DeptId

		this_plant = Plant.query.first()
		order_invoice_data["PlantId"] = this_plant.PlantId

		OInvGuid = order_invoice_data['OInvGuid']
		OInvRegNo = order_invoice_data['OInvRegNo']

		thisOrderInv = Order_inv.query\
			.filter_by(
				OInvGuid = OInvGuid)\
			.first()

		if thisOrderInv:
			order_invoice_data['OInvId'] = thisOrderInv.OInvId
			thisOrderInv.update(**order_invoice_data)
			db.session.commit()

		else:
			thisOrderInv = Order_inv(**order_invoice_data)
			db.session.add(thisOrderInv)
			db.session.commit()

		data, fails = save_order_line_synch_data(
			req = order_inv_lines_req,
			OInvId = thisOrderInv.OInvId
		)

		if fails:
			res = {
				"data": order_invoice_data,
				"successes": data,
				"fails": fails,
				"success_total": len(data),
				"fail_total": len(fails),
				"total": len(order_inv_lines_req)
			}

			db.session.delete(thisOrderInv)
			db.session.commit()

		else:
			db.session.commit()

			res = {
				"data": thisOrderInv.to_json_api(),
				"successes": data,
				"fails": fails,
				"success_total": len(data),
				"fail_total": len(fails) or 0,
				"total": len(order_inv_lines_req)
			}

		order_invoice_data['Order_inv_lines'] = data

	except Exception as ex:
		print(f"{datetime.now()} | OInv Api Exception: {ex}")
		res = {
			"data": order_invoice_data,
			"message": "Failed to checkout order",
			"status": 0,
		}

	return res