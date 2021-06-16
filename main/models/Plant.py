from sqlalchemy.dialects.postgresql import UUID

from main import db

class Plant(db.Model):
	__tablename__ = "tbl_mg_plant"
	PlantId = db.Column("plant_id",db.Integer,nullable=False,primary_key=True)
	PlantGuid = db.Column("plant_id_guid",UUID(as_uuid=True),unique=True)
	PlantName = db.Column("plant_name",db.String)

	def to_json(self):
		data = {
			"PlantId": self.PlantId,
			"PlantGuid": self.PlantGuid,
			"PlantName": self.PlantName,
		}

		return data