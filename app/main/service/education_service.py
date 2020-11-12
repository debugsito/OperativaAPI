import uuid
import datetime

from app.main import db
from app.main.model.education import Education
from flask import request

from app.main.service.auth_helper import Auth


def save_new_education(data):
    data_session, status = Auth.get_logged_in_account(request)
    account_id = data_session.get('data').get('account_id')
    new_education = Education(
        id_account=account_id,
        level=data['level'],
        name_inst=data['name_inst'],
        field=data['field'],
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


def get_all_education():
    return Education.query.all()


def get_a_education(id_account):
    return Education.query.filter_by(id_account=id_account).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

