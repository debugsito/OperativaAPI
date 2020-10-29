
from .. import db

class Provider(db.Model):
	""" Provider Model for storing education related details """
	__tablename__ = "provider"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(1000), nullable=False)
	description = db.Column(db.String(1000), nullable=False)
	
	
	def __repr__(self):
		return "<Document '{}'>".format(self.name)
