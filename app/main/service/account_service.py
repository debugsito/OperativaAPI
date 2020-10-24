import uuid
import datetime

from app.main import db
from app.main.model.account import Account


def save_account(data):
    account = Account.query.filter_by(email=data['email']).first()
    if not account:
        new_account = Account(
            email=data['email'],
            password=data['password'],
			old_password = "",
			term_condi = data['term_condi'],
			wrong_login_attempt = None,
			today_login_attempt =  datetime.datetime.now(),
			is_now_login = 1,
            registered_on=  datetime.datetime.now()
        )
        save_changes(new_account)
        return generate_token(new_account)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Account already exists. Please Log in.',
        }
        return response_object, 409


def get_all_accounts():
    return Account.query.all()


def get_a_account(email):
    return Account.query.filter_by(email=email).first()


def generate_token(account):
    try:
        # generate the auth token
        auth_token = Account.encode_auth_token(account.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

