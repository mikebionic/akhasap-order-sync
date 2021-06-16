from sqlalchemy.dialects.postgresql import UUID

from main import db

class Warehouse(db.Model):
	__tablename__ = "tbl_mg_whouse"
	WhId = db.Column("wh_id",db.Integer,nullable=False,primary_key=True)
	WhGuid = db.Column("wh_id_guid",UUID(as_uuid=True),unique=True)
	WhName = db.Column("wh_name",db.String)

	def to_json(self):
		data = {
			"WhId": self.WhId,
			"WhGuid": self.WhGuid,
			"WhName": self.WhName,
		}

		return data