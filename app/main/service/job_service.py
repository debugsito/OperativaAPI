import uuid
import datetime

from app.main import db
from app.main.model.job import Job

def save_new_job(data):
    if data["id_account"] > 0:
        new_job = Job(
			id_account = data['id_account'],
			name_inst=data['name_inst'],
			department=data['department'],
			job_level = data['job_level'],
			from_year=data['from_year'],
			to_year=data['to_year'],
			buss_travel=data['buss_travel'],
			distan_home=data['distan_home'],
			hour_rate=data['hour_rate'],
			job_role=data['job_role'],
			job_sati=data['job_sati'],
			monthly_income=data['monthly_income'],
			over_time=data['over_time'],
			work_bal_life=data['work_bal_life'],
			job_invol=data['job_invol'],
			attrition=data['attrition'],
            registered_on=datetime.datetime.now()
        )
        save_changes(new_job)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Job already exists. Please Log in.',
        }
        return response_object, 409


def get_all_job():
    return Job.query.all()


def get_a_job(id_account):
    return Job.query.filter_by(id_account=id_account)


def save_changes(data):
    db.session.add(data)
    db.session.commit()

