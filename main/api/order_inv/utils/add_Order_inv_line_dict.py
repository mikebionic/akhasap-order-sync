# -*- coding: utf-8 -*-
import uuid

def add_Order_inv_line_dict(req):
	OInvLineId = req.get('OInvLineId')
	OInvLineGuid = uuid.UUID(req.get('OInvLineGuid'))
	OInvId = req.get('OInvId')
	UnitId = req.get('UnitId')
	ResId = req.get('ResId')
	OInvLineRegNo = req.get('OInvLineRegNo')
	OInvLineDesc = req.get('OInvLineDesc')
	OInvLineAmount = req.get('OInvLineAmount')
	OInvLinePrice = req.get('OInvLinePrice')
	OInvLineTotal = req.get('OInvLineTotal')
	OInvLineDiscAmount = req.get('OInvLineDiscAmount')
	OInvLineFTotal = req.get('OInvLineFTotal')
	OInvLineDate = req.get('OInvLineDate')

	data = {
		"OInvLineGuid": OInvLineGuid,
		"OInvId": OInvId,
		"UnitId": UnitId,
		"ResId": ResId,
		"OInvLineRegNo": OInvLineRegNo,
		"OInvLineDesc": OInvLineDesc,
		"OInvLineAmount": OInvLineAmount,
		"OInvLinePrice": OInvLinePrice,
		"OInvLineTotal": OInvLineTotal,
		"OInvLineDiscAmount": OInvLineDiscAmount,
		"OInvLineFTotal": OInvLineFTotal,
		"OInvLineDate": OInvLineDate,
	}

	return data