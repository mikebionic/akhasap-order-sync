from sqlalchemy.dialects.postgresql import UUID

from main import db

class Unit(db.Model):
	__tablename__ = "tbl_mg_units"
	UnitId = db.Column("unit_id",db.Integer,nullable=False,primary_key=True)
	UnitGuid = db.Column("unit_id_guid",UUID(as_uuid=True),unique=True)
	UnitName = db.Column("unit_name",db.String)

	def to_json(self):
		data = {
			"UnitId": self.UnitId,
			"UnitGuid": self.UnitGuid,
			"UnitName": self.UnitName,
		}

		return data