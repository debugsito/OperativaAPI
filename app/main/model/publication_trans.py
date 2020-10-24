
from .. import db
import datetime

class Publication_trans(db.Model):
	""" Publication_trans Model for storing publication related details """
	__tablename__ = "publication_trans"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	id_publication = db.Column(db.Integer, nullable=False)
	id_user = db.Column(db.Integer, nullable=False)
	description = db.Column(db.String(1000), nullable=False)
	status = db.Column(db.Integer, nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)
	
	def __repr__(self):
		return "<Enterprise '{}'>".format(self.id)
