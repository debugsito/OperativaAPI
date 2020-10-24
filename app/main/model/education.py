
from .. import db
import datetime

class Education(db.Model):
	""" Education Model for storing account related details """
	__tablename__ = "education"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	id_account = db.Column(db.Integer, nullable=False)
	level = db.Column(db.Integer, nullable=False)
	name_inst = db.Column(db.String(300), nullable=False)
	field = db.Column(db.Integer)
	from_year = db.Column(db.String(300), nullable=False)
	to_year = db.Column(db.String(300), nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)
	
	def __repr__(self):
		return "<Education '{}'>".format(self.id)
