import uuid
import datetime

from app.main import db
from app.main.model.publication_trans import Publication_trans


def save_new_publication_trans(data):
    if data["id_publication"] > 0:
        new_publication_trans = Publication_trans(
			id_publication = data['id_publication'],
			id_user=data['id_user'],
			description=data['description'],
			status=1,
            registered_on=datetime.datetime.now()
        )
        save_changes(new_publication_transs)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Publication_trans already exists. Please Log in.',
        }
        return response_object, 409


def get_all_publication_trans():
    return Publication_trans.query.all()


def get_a_publication_trans(id_publication):
    return Publication_trans.query.filter_by(id_publication=id_publication)


def save_changes(data):
    db.session.add(data)
    db.session.commit()

