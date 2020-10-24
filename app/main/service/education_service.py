import uuid
import datetime

from app.main import db
from app.main.model.education import Education


def save_new_education(data):
    if data["id_account"] > 0:
        new_education = Education(
			id_account = data['id_account'],
			level=data['level'],
			name_inst=data['name_inst'],
			field = data['field'],
            from_year=data['from_year'],
            to_year=data['to_year'],
            registered_on=datetime.datetime.now()
        )
        save_changes(new_education)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Education already exists. Please Log in.',
        }
        return response_object, 409


def get_all_education():
    return Education.query.all()


def get_a_education(id_account):
    return Education.query.filter_by(id_account=id_account).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

