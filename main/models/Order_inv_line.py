from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db


class Order_inv_line(db.Model):
	__tablename__ = "tbl_mg_fich_line"
	OInvLineId = db.Column("fich_line_id",db.Integer,nullable=False,primary_key=True)
	OInvLineGuid = db.Column("fich_line_guid",UUID(as_uuid=True),unique=True)
	OInvId = db.Column("fich_id",db.Integer)
	# UnitId = db.Column("UnitId",db.Integer)
	# CurrencyId = db.Column("CurrencyId",db.Integer)
	ResId = db.Column("material_id",db.Integer)
	# LastVendorId = db.Column("LastVendorId",db.Integer)
	OInvLineRegNo = db.Column("fich_line_code",db.String(100),nullable=False,unique=True)
	OInvLineDesc = db.Column("fich_line_desc",db.String(500))
	OInvLineAmount = db.Column("fich_line_amount",db.Float,default=0.0)
	OInvLinePrice = db.Column("fich_line_price",db.Float,default=0.0)
	OInvLineTotal = db.Column("fich_line_total",db.Float,default=0.0)
	# OInvLineExpenseAmount = db.Column("OInvLineExpenseAmount",db.Float,default=0.0)
	# OInvLineTaxAmount = db.Column("OInvLineTaxAmount",db.Float,default=0.0)
	OInvLineDiscAmount = db.Column("fich_line_disc_amount",db.Float,default=0.0)
	OInvLineFTotal = db.Column("fich_line_nettotal",db.Float,default=0.0)
	OInvLineDate = db.Column("fich_line_date",db.DateTime,default=datetime.now)
	# ExcRateValue = db.Column("ExcRateValue",db.Float,default=0.0)

	def to_json(self):
		data = {
			"OInvLineId": self.OInvLineId,
			"OInvLineGuid": self.OInvLineGuid,
			"OInvId": self.OInvId,
			"ResId": self.ResId,
			"OInvLineRegNo": self.OInvLineRegNo,
			"OInvLineDesc": self.OInvLineDesc,
			"OInvLineAmount": self.OInvLineAmount,
			"OInvLinePrice": self.OInvLinePrice,
			"OInvLineTotal": self.OInvLineTotal,
			"OInvLineDiscAmount": self.OInvLineDiscAmount,
			"OInvLineFTotal": self.OInvLineFTotal,
			"OInvLineDate": self.OInvLineDate,
		}

		return data



# int fich_line_id
# Guid fich_line_guid
# string fich_line_code
# float fich_line_amount
# float fich_line_price
# float fich_line_total
# int inv_id
# int fich_id
# int material_id
# string fich_line_desc
# float fich_line_disc_amount
# float fich_line_nettotal
# DateTime fich_line_date

# # # ???
# int unit_det_id
# float fich_line_disc_prc
# int service_id
# DateTime fich_line_expiredate
# string fich_line_serialno
# int mat_inv_line_id
# float rep_rate
# float rep_total
# string spe_code
# string group_code
# string security_code
# int fich_line_type_id
