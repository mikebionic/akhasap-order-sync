from sqlalchemy.dialects.postgresql import UUID

from main import db

class User(db.Model):
	__tablename__ = "tbl_mg_salesman"
	UId = db.Column("salesman_id",db.Integer,nullable=False,primary_key=True)
	UGuid = db.Column("salesman_id_guid",UUID(as_uuid=True),unique=True)
	UName = db.Column("salesman_name",db.String)

	def to_json(self):
		data = {
			"UId": self.UId,
			"UGuid": self.UGuid,
			"UName": self.UName,
		}

		return data