
from .. import db
import datetime

class Job(db.Model):
	""" job Model for storing account related details """
	__tablename__ = "job"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	id_account = db.Column(db.Integer, nullable=False)
	name_inst = db.Column(db.String(100), nullable=False)
	department = db.Column(db.Integer)
	job_level = db.Column(db.Integer)
	from_year = db.Column(db.String(100))
	to_year = db.Column(db.String(100))
	buss_travel = db.Column(db.Integer)
	distan_home = db.Column(db.Float)
	hour_rate = db.Column(db.Float)
	job_role = db.Column(db.Integer)
	job_sati = db.Column(db.Integer)
	monthly_income = db.Column(db.Float)
	over_time = db.Column(db.Integer)
	work_bal_life = db.Column(db.Integer)
	job_invol = db.Column(db.Integer)
	attrition = db.Column(db.Integer)
	registered_on = db.Column(db.DateTime, nullable=False)
	
	
	def __repr__(self):
		return "<User '{}'>".format(self.id)
