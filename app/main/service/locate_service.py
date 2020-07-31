import uuid
import datetime

from app.main import db
from app.main.model.locate import Country, State, City


def get_all_contries():
    return Country.query.all()

def get_all_states():
    return State.query.all()	

def get_all_cities():
	return City.query.all()

