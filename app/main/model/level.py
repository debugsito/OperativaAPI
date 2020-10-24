
from .. import db

class Level(db.Model):
	""" Level Model for storing education related details """
	__tablename__ = "level"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(100), nullable=False)
	
	
	def __repr__(self):
		return "<Document '{}'>".format(self.name)
