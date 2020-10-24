import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    if data["id_account"] > 0:
        new_user = User(
			id_account = data['id_account'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			gender = data['gender'],
			type_doc=data['type_doc'],
			num_doc=data['num_doc'],
			birth_date=data['birth_date'],
			address=data['address'],
			phone=data['phone'],
			id_country=data['id_country'],
			id_state=data['id_state'],
			id_city=data['id_city'],
			id_civil_status=data['id_civil_status'],
			id_provider=data['id_provider'],
            registered_on=datetime.datetime.now()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(id_account):
    return User.query.filter_by(id_account=id_account).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

