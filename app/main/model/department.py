
from .. import db

class Department(db.Model):
	""" Department Model for storing job related details """
	__tablename__ = "department"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(100), nullable=False)
	
	
	def __repr__(self):
		return "<Document '{}'>".format(self.name)
