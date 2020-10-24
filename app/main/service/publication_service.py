import uuid
import datetime

from app.main import db
from app.main.model.publication import Publication


def save_new_publication(data):
    if data["id_enterprise"] > 0:
        new_publication = Publication(
			id_enterprise = data['id_enterprise'],
			description=data['description'],
			from_date=data['from_date'],
			to_date=data['to_date'],
			job_role=data['job_role'],
			type_job=data['type_job'],
			salary=data['salary'],
			url=data['url'],
			status=1,
            registered_on=datetime.datetime.now()
        )
        save_changes(new_publication)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Publication already exists. Please Log in.',
        }
        return response_object, 409


def get_all_publication():
    return Publication.query.all()


def get_a_publication(id_enterprise):
    return Publication.query.filter_by(id_enterprise=id_enterprise).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

