
from .. import db
import datetime

class User(db.Model):
	""" User Model for storing account related details """
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	id_account = db.Column(db.Integer, unique=True, nullable=False)
	first_name = db.Column(db.String(100), nullable=False)
	last_name = db.Column(db.String(100), nullable=False)
	gender = db.Column(db.Integer, nullable=False)
	type_doc = db.Column(db.Integer, nullable=False)
	num_doc = db.Column(db.String(30), unique=True, nullable=False)
	birth_date = db.Column(db.String(30), nullable=False)
	address = db.Column(db.String(300), nullable=False)
	phone = db.Column(db.String(20), unique=True, nullable=False)
	id_country = db.Column(db.Integer, nullable=False)
	id_state = db.Column(db.Integer, nullable=False)
	id_city = db.Column(db.Integer, nullable=False)
	id_civil_status = db.Column(db.Integer, nullable=False)
	id_provider = db.Column(db.Integer, nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)
	
	
	def __repr__(self):
		return "<User '{}'>".format(self.first_name)
