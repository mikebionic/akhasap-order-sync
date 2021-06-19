# -*- coding: utf-8 -*-
import uuid

def add_Order_inv_dict(req):
	OInvId = req.get('OInvId')
	OInvGuid = uuid.UUID(req.get('OInvGuid'))
	OInvTypeId = req.get('OInvTypeId')
	InvStatId = req.get('InvStatId')
	RpAccId = req.get('RpAccId')
	UId = req.get('UId')
	DivId = req.get('DivId')
	WhId = req.get('WhId')
	OInvLatitude = req.get('OInvLatitude')
	OInvLongitude = req.get('OInvLongitude')
	OInvRegNo = req.get('OInvRegNo')
	OInvDesc = req.get('OInvDesc')
	OInvDate = req.get('OInvDate')
	OInvTotal = req.get('OInvTotal')
	OInvDiscountAmount = req.get('OInvDiscountAmount')
	OInvFTotal = req.get('OInvFTotal')
	OInvFTotalInWrite = req.get('OInvFTotalInWrite')
	CreatedDate = req.get('CreatedDate')
	ModifiedDate = req.get('ModifiedDate')
	SyncDateTime = req.get('SyncDateTime')

	data = {
		"OInvGuid": OInvGuid,
		"OInvTypeId": OInvTypeId,
		"InvStatId": InvStatId,
		"RpAccId": RpAccId,
		"UId": UId,
		"DivId": DivId,
		"WhId": WhId,
		"OInvLatitude": OInvLatitude,
		"OInvLongitude": OInvLongitude,
		"OInvRegNo": OInvRegNo,
		"OInvDesc": OInvDesc,
		"OInvDate": OInvDate,
		"OInvTotal": OInvTotal,
		"OInvDiscountAmount": OInvDiscountAmount,
		"OInvFTotal": OInvFTotal,
		"OInvFTotalInWrite": OInvFTotalInWrite,
		"CreatedDate": CreatedDate,
		"ModifiedDate": ModifiedDate,
		"SyncDateTime": SyncDateTime,
	}

	return data