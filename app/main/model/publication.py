
from .. import db
import datetime

class Publication(db.Model):
	""" Publication Model for storing enterprise related details """
	__tablename__ = "publication"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	id_enterprise = db.Column(db.Integer, nullable=False)
	description = db.Column(db.String(10000), nullable=False)
	from_date = db.Column(db.String(30), nullable=False)
	to_date = db.Column(db.String(300), nullable=False)
	job_role = db.Column(db.Integer, nullable=False)
	type_job = db.Column(db.Integer, nullable=False)
	salary = db.Column(db.Integer, nullable=False)
	url = db.Column(db.String(500), nullable=False)
	status = db.Column(db.Integer, nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)
	
	def __repr__(self):
		return "<Enterprise '{}'>".format(self.id)
