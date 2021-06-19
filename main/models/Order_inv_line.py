from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db

# required to set:
# OInvId
# ResId from resource GUID

# probably needed:
# UnitId (fist(san))


class Order_inv_line(db.Model):
	__tablename__ = "tbl_mg_order_fich_line"
	OInvLineId = db.Column("fich_line_id",db.Integer,nullable=False,primary_key=True)
	OInvLineGuid = db.Column("OInvLineGuid",UUID(as_uuid=True),unique=True)
	OInvId = db.Column("fich_id",db.Integer)
	UnitId = db.Column("unit_det_id",db.Integer,default=1)
	# CurrencyId = db.Column("CurrencyId",db.Integer)
	ResId = db.Column("material_id",db.Integer)
	# LastVendorId = db.Column("LastVendorId",db.Integer)
	# OInvLineRegNo = db.Column("fich_line_code",db.String(100),nullable=False,unique=True)
	OInvLineDesc = db.Column("fich_line_desc",db.String(500),default='')
	OInvLineAmount = db.Column("fich_line_amount",db.Float,default=0.0)
	OInvLinePrice = db.Column("fich_line_price",db.Float,default=0.0)
	OInvLineTotal = db.Column("fich_line_total",db.Float,default=0.0)
	# OInvLineExpenseAmount = db.Column("OInvLineExpenseAmount",db.Float,default=0.0)
	# OInvLineTaxAmount = db.Column("OInvLineTaxAmount",db.Float,default=0.0)
	OInvLineDiscAmount = db.Column("fich_line_disc_amount",db.Float,default=0.0)
	OInvLineFTotal = db.Column("fich_line_nettotal",db.Float,default=0.0)
	OInvLineDate = db.Column("fich_line_date",db.DateTime,default=datetime.now)
	ExcRateValue = db.Column("rep_rate",db.Float,default=0.0)
	rep_total = db.Column("rep_total",db.Float,default=0.0)

	fich_line_disc_prc = db.Column("fich_line_disc_prc",db.Float,default=0.0)
	inv_id = db.Column("inv_id",db.Integer,default=0)
	service_id = db.Column("service_id",db.Integer,default=0)
	fich_line_expiredate = db.Column("fich_line_expiredate",db.DateTime)
	fich_line_type_id = db.Column("fich_line_type_id",db.Integer,default=0)
	fich_line_serialno = db.Column("fich_line_serialno",db.String,default="")
	mat_inv_line_id = db.Column("mat_inv_line_id",db.Integer,default=0)
	# fich_line_cost = db.Column("fich_line_cost",db.Integer,default=0)
	# arap_id_ventor = db.Column("arap_id_ventor",db.Integer,default=0)

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

	def to_json(self):
		data = {
			"OInvLineId": self.OInvLineId,
			"OInvLineGuid": self.OInvLineGuid,
			"OInvId": self.OInvId,
			"UnitId": self.UnitId,
			"ResId": self.ResId,
			# "OInvLineRegNo": self.OInvLineRegNo,
			"OInvLineDesc": self.OInvLineDesc,
			"OInvLineAmount": self.OInvLineAmount,
			"OInvLinePrice": self.OInvLinePrice,
			"OInvLineTotal": self.OInvLineTotal,
			"OInvLineDiscAmount": self.OInvLineDiscAmount,
			"OInvLineFTotal": self.OInvLineFTotal,
			"OInvLineDate": self.OInvLineDate,
		}

		return data