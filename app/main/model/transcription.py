
from .. import db
import datetime

class Transcription(db.Model):
	""" Transcription Model for storing user related details """
	__tablename__ = "transcription"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	id_user = db.Column(db.Integer, nullable=False)
	audio_name = db.Column(db.String(100), default='', nullable=False)
	audio_url = db.Column(db.String(300), default='', nullable=False)
	id_language_source = db.Column(db.Integer, nullable=False)
	id_language_target = db.Column(db.Integer, nullable=False)
	phrase_trans = db.Column(db.String(30000), default='', nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)
	
	def __repr__(self):
		return "<Transcription '{}'>".format(self.audio_name)
