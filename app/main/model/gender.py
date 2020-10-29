
from .. import db

class Gender(db.Model):
	""" Gender Model for storing education related details """
	__tablename__ = "gender"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(100), nullable=False)
	
	
	def __repr__(self):
		return "<Document '{}'>".format(self.name)
