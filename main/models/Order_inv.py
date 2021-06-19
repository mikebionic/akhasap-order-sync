from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db

# should be fetched:
# RpAccId from rp_acc arap GUID
# DivId from Division	GUID
# WhId from warehouse GUID
# UId from Users (salesmanId GUID)
# WpId from period p_id (first)

# todo
# fich_total_unit_amount = len(oinvlines)

# probably need to
# dept_id from department (new akh model)
# plant_id from plant (new akh model)


class Order_inv(db.Model):
	__tablename__ = "tbl_mg_order_fich"
	OInvId = db.Column("fich_id",db.Integer,nullable=False,primary_key=True)
	OInvGuid = db.Column("fich_id_guid",UUID(as_uuid=True),unique=True)
	OInvTypeId = db.Column("fich_type_id",db.Integer,default=12)
	InvStatId = db.Column("ord_status_id",db.Integer,default=0)
	# CurrencyId = db.Column("CurrencyId",db.Integer)
	RpAccId = db.Column("arap_id",db.Integer)
	# CId = db.Column("CId",db.Integer)
	UId = db.Column("salesman_id",db.Integer,default=1)
	DivId = db.Column("div_id",db.Integer,default=1)
	WhId = db.Column("wh_id",db.Integer,default=1)
	WpId = db.Column("p_id",db.Integer,default=1)
	# EmpId = db.Column("EmpId",db.Integer)
	# PtId = db.Column("PtId",db.Integer)
	# PmId = db.Column("PmId",db.Integer)
	# PaymStatusId = db.Column("PaymStatusId",db.Integer)
	# PaymCode = db.Column("PaymCode",db.String(500))
	# PaymDesc = db.Column("PaymDesc",db.String(500))
	OInvLatitude = db.Column("order_lat",db.Float,default=0.0)
	OInvLongitude = db.Column("order_long",db.Float,default=0.0)
	OInvRegNo = db.Column("fich_code",db.String(100),nullable=False,unique=True)
	OInvDesc = db.Column("fich_desc",db.String(500))
	OInvDate = db.Column("fich_date",db.DateTime,default=datetime.now)
	OInvTotal = db.Column("fich_total",db.Float,default=0.0)
	# OInvExpenseAmount = db.Column("OInvExpenseAmount",db.Float,default=0.0)
	# OInvTaxAmount = db.Column("OInvTaxAmount",db.Float,default=0.0)
	OInvDiscountAmount = db.Column("fich_discount",db.Float,default=0.0)
	# OInvPaymAmount = db.Column("OInvPaymAmount",db.Float,default=0.0)
	OInvFTotal = db.Column("fich_nettotal",db.Float,default=0.0)
	OInvFTotalInWrite = db.Column("fich_nettotal_text",db.String(100))
	# OInvModifyCount = db.Column("OInvModifyCount",db.Integer,default=0)
	# OInvPrintCount = db.Column("OInvPrintCount",db.Integer,default=0)
	# OInvCreditDays = db.Column("OInvCreditDays",db.Integer,default=0)
	# OInvCreditDesc = db.Column("OInvCreditDesc",db.String(100))
	CreatedDate = db.Column("fich_create_date",db.DateTime,default=datetime.now())
	ModifiedDate = db.Column("fich_modify_date",db.DateTime,default=datetime.now(),onupdate=datetime.now())
	SyncDateTime = db.Column("sync_datetime",db.DateTime,default=datetime.now())

	rep_rate = db.Column("rep_rate",db.Float,default=0.0)
	rep_total = db.Column("rep_total",db.Float,default=0.0)
	DeptId = db.Column("dept_id",db.Integer,default=1)
	PlantId = db.Column("plant_id",db.Integer,default=1)
	inv_id = db.Column("inv_id",db.Integer,default=0)
	T_ID = db.Column("T_ID",db.Integer,default=0)
	payplan_id = db.Column("payplan_id",db.Integer,default=0)
	fich_total_unit_amount = db.Column("fich_total_unit_amount",db.Float,default=0.0)
	fich_modified = db.Column("fich_modified",db.Integer,default=0)
	bank_acc_id_client = db.Column("bank_acc_id_client",db.Integer,default=0)
	bank_acc_id_local = db.Column("bank_acc_id_local",db.Integer,default=0)
	delivery_arap_id = db.Column("delivery_arap_id",db.Integer,default=0)

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

	def to_json(self):
		data = {
			"OInvId": self.OInvId,
			"OInvGuid": self.OInvGuid,
			"OInvTypeId": self.OInvTypeId,
			"InvStatId": self.InvStatId,
			"RpAccId": self.RpAccId,
			"UId": self.UId,
			"DivId": self.DivId,
			"WhId": self.WhId,
			"OInvLatitude": self.OInvLatitude,
			"OInvLongitude": self.OInvLongitude,
			"OInvRegNo": self.OInvRegNo,
			"OInvDesc": self.OInvDesc,
			"OInvDate": self.OInvDate,
			"OInvTotal": self.OInvTotal,
			"OInvDiscountAmount": self.OInvDiscountAmount,
			"OInvFTotal": self.OInvFTotal,
			"OInvFTotalInWrite": self.OInvFTotalInWrite,
			"CreatedDate": self.CreatedDate,
			"ModifiedDate": self.ModifiedDate,
			"SyncDateTime": self.SyncDateTime,
		}

		return data