
from .. import db

class Job_role(db.Model):
	""" Job_role Model for storing job related details """
	__tablename__ = "job_role"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(100), nullable=False)
	
	
	def __repr__(self):
		return "<Document '{}'>".format(self.name)
