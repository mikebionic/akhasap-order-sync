from sqlalchemy.dialects.postgresql import UUID

from main import db

class Department(db.Model):
	__tablename__ = "tbl_mg_department"
	DeptId = db.Column("dept_id",db.Integer,nullable=False,primary_key=True)
	DeptGuid = db.Column("dept_id_guid",UUID(as_uuid=True),unique=True)
	DeptName = db.Column("dept_name",db.String)

	def to_json(self):
		data = {
			"DeptId": self.DeptId,
			"DeptGuid": self.DeptGuid,
			"DeptName": self.DeptName,
		}

		return data