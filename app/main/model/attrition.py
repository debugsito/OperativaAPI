
from .. import db

class Attrition(db.Model):
	""" Attrition Model for storing job related details """
	__tablename__ = "attrition"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(100), nullable=False)
	
	
	def __repr__(self):
		return "<Document '{}'>".format(self.name)
