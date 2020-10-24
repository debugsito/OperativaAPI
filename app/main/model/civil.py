
from .. import db

class Civil(db.Model):
	""" Civil for storing user related details """
	__tablename__ = "civil"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(100), nullable=False)
	
	
	def __repr__(self):
		return "<Civil status '{}'>".format(self.name)
