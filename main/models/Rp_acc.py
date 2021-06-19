from sqlalchemy.dialects.postgresql import UUID

from main import db

class Rp_acc(db.Model):
	__tablename__ = "tbl_mg_arap"
	RpAccId = db.Column("arap_id",db.Integer,nullable=False,primary_key=True)
	RpAccGuid = db.Column("RpAccGuid",UUID(as_uuid=True),unique=True)
	RpAccName = db.Column("arap_name",db.String)

	def to_json(self):
		data = {
			"RpAccId": self.RpAccId,
			"RpAccGuid": self.RpAccGuid,
			"RpAccName": self.RpAccName,
		}

		return data