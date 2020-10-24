
from .. import db

class Document(db.Model):
	""" Document Model for storing user related details """
	__tablename__ = "document"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(100), nullable=False)
	
	
	def __repr__(self):
		return "<Document '{}'>".format(self.name)
