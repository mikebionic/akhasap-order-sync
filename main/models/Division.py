from sqlalchemy.dialects.postgresql import UUID

from main import db

class Division(db.Model):
	__tablename__ = "tbl_mg_division"
	DivId = db.Column("div_id",db.Integer,nullable=False,primary_key=True)
	DivGuid = db.Column("div_id_guid",UUID(as_uuid=True),unique=True)
	DivName = db.Column("div_name",db.String)

	def to_json(self):
		data = {
			"DivId": self.DivId,
			"DivGuid": self.DivGuid,
			"DivName": self.DivName,
		}

		return data