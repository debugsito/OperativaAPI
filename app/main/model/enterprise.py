
from .. import db
import datetime

class Enterprise(db.Model):
	""" Enterprise Model for storing enterprise related details """
	__tablename__ = "enterprise"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	id_account = db.Column(db.Integer, unique=True, nullable=False)
	name = db.Column(db.String(300), nullable=False)
	ruc = db.Column(db.String(30), unique=True, nullable=False)
	address = db.Column(db.String(300), nullable=False)
	phone = db.Column(db.String(20), unique=True, nullable=False)
	fax = db.Column(db.String(20), unique=True, nullable=False)
	type_job = db.Column(db.Integer, nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)
	
	def __repr__(self):
		return "<Enterprise '{}'>".format(self.id)
