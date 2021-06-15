from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db


class Order_inv(db.Model):
	__tablename__ = "tbl_mg_order_fich"
	OInvId = db.Column("fich_id",db.Integer,nullable=False,primary_key=True)
	OInvGuid = db.Column("fich_id_guid",UUID(as_uuid=True),unique=True)
	OInvTypeId = db.Column("fich_type_id")
	InvStatId = db.Column("ord_status_id")
	# CurrencyId = db.Column("CurrencyId")
	RpAccId = db.Column("arap_id")
	# CId = db.Column("CId")
	UId = db.Column("salesman_id")
	DivId = db.Column("div_id")
	WhId = db.Column("wh_id")
	# WpId = db.Column("WpId")
	# EmpId = db.Column("EmpId")
	# PtId = db.Column("PtId")
	# PmId = db.Column("PmId")
	# PaymStatusId = db.Column("PaymStatusId")
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
		}

		return data


# # Done
# int fich_id
# Guid OInvGuid
# string fich_code
# DateTime fich_date
# float fich_total
# DateTime fich_create_date
# int fich_type_id
# int arap_id
# int div_id
# int wh_id

# string fich_desc
# float fich_discount
# float fich_nettotal
# string fich_nettotal_text
# int salesman_id
# int ord_status_id
# float order_lat
# float order_long
# DateTime fich_modify_date
# DateTime sync_datetime
# # Done


# ???????
# int dept_id
# int plant_id
# int p_id
# int inv_id
# int T_ID
# ????????

# string spe_code
# string group_code
# string security_code
# int payplan_id
# float rep_rate
# float rep_total
# float fich_total_unit_amount
# int fich_modified
# int bank_acc_id_client
# int bank_acc_id_local
# int delivery_arap_id