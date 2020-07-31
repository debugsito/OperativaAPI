
from .. import db
import datetime

class Country(db.Model):
	""" Countries Model by located details """
	__tablename__ = "countries"
	id = db.Column(db.Integer, primary_key=True)
	sort_name = db.Column(db.String(3), nullable=False)
	name = db.Column(db.String(150), nullable=False)
	phone_code = db.Column(db.Integer, nullable=False)
	
	def __repr__(self):
		return "<Country '{}'>".format(self.name)

class State(db.Model):
	""" States Model by located details """
	__tablename__ = "states"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	id_country = db.Column(db.Integer, nullable=False)
	
	def __repr__(self):
		return "<State '{}'>".format(self.name)

class City(db.Model):
	""" Cities Model by located details """
	__tablename__ = "cities"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	id_state = db.Column(db.Integer, nullable=False)
	
	def __repr__(self):
		return "<City '{}'>".format(self.name)