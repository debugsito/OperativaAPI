import datetime
from app.extensions import db

class User(db.Model):
	"""User database Model"""
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(column_types.PasswordType(max_length=128,schemes=('bcrypt', )),nullable=False)
	first_name = db.Column(db.String(30), default='', nullable=False)
	middle_name = db.Column(db.String(30), default='', nullable=False)
	last_name = db.Column(db.String(30), default='', nullable=False)
	type_doc = db.Column(db.Integer, nullable=False)
	num_doc = db.Column(db.String(30), unique=True, nullable=False)
	id_country = db.Column(db.Integer, nullable=False)
	id_state = db.Column(db.Integer, nullable=False)
	id_city = db.Column(db.Integer, nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)
	public_id = db.Column(db.String(100), unique=True)
	
	@property
	def password(self):
		raise AttributeError('password: write-only field')
	
	@password.setter
	def password(self, password):
		self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
		
	def check_password(self, password):
		return flask_bcrypt.check_password_hash(self.password_hash, password)
	
	@classmethod
	def find_with_password(cls, email, password):
		user = cls.query.filter_by(email=email).first()
		if not user:
			return None
		if user.password == password:
			return user
		return None