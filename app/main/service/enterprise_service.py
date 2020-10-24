import uuid
import datetime

from app.main import db
from app.main.model.enterprise import Enterprise


def save_new_enterprise(data):
    if data["id_account"] > 0:
        new_enterprise = Enterprise(
			id_account = data['id_account'],
			name=data['name'],
			ruc=data['ruc'],
			address=data['address'],
			phone=data['phone'],
			fax=data['fax'],
			type_job=data['type_job'],
            registered_on=datetime.datetime.now()
        )
        save_changes(new_enterprise)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Enterprise already exists. Please Log in.',
        }
        return response_object, 409


def get_all_enterprise():
    return Enterprise.query.all()


def get_a_enterprise(id_account):
    return Enterprise.query.filter_by(id_account=id_account).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

