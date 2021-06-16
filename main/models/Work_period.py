from sqlalchemy.dialects.postgresql import UUID

from main import db

class Work_period(db.Model):
	__tablename__ = "tbl_mg_period"
	WpId = db.Column("p_id",db.Integer,nullable=False,primary_key=True)
	WpGuid = db.Column("p_id_guid",UUID(as_uuid=True),unique=True)

	def to_json(self):
		data = {
			"WpId": self.WpId,
			"WpGuid": self.WpGuid,
		}

		return data