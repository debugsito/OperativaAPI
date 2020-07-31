import datetime
import os
import librosa
from time import gmtime, strftime
from random import randint
import re, string

from app.main import db
from app.main.model.transcription import Transcription


ALLOWED_EXTENSIONS = set(['wav', 'ogg', 'mp', 'mp3', 'mp4'])

def save_new_transcription(audio_name,url):
	phrase_trans = audio_transcription(url+"/"+audio_name)
	data = audio_name.split('_')
	new_transcription = Transcription(
		id_user=data[0],
		audio_name=audio_name,
		audio_url=url,
		id_language_source=data[1],
		id_language_target=data[2],
		phrase_trans=phrase_trans,
		registered_on=datetime.datetime.utcnow()
	)
	save_changes(new_transcription)
	return get_transcription(audio_name)


def audio_transcription(audio):
	y, sr = librosa.load(audio)
	os.system("sox "+audio+" -r 16000 -c 1 -b 16 result.wav")
	os.system("deepspeech output_graph.pb quz_alphabet.txt result.wav >> result.txt")
	file_trans = open("result.txt", "r") 
	phrase_trans = file_trans.read()
	os.system("rm result.txt")
	return phrase_trans

	
def get_transcription(audio_name):
    return Transcription.query.filter_by(audio_name=audio_name).first()

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS	
	
def createFile():
    timer = strftime("%d-%m-%Y", gmtime())
    date = timer.replace("-","_")
    return date
	
def save_changes(data):
    db.session.add(data)
    db.session.commit()

