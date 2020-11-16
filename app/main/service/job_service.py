import uuid
import datetime

from app.main import db
from app.main.model.job import Job
from flask import request

from app.main.service.auth_helper import Auth

def save_new_job(data):
    data_session, status = Auth.get_logged_in_account(request)
    account_id = data_session.get('data').get('account_id')
    if(isinstance(data, list)):
        for job in data:
            new_job = Job(
                id_account=account_id,
                name_inst=job['name_inst'],
                department=job['department'],
                job_level=job['job_level'],
                from_year=job['from_year'],
                to_year=job['to_year'],
                buss_travel=job['buss_travel'],
                distan_home=job['distan_home'],
                hour_rate=job['hour_rate'],
                job_role=job['job_role'],
                job_sati=job['job_sati'],
                monthly_income=job['monthly_income'],
                over_time=job['over_time'],
                work_bal_life=job['work_bal_life'],
                job_invol=job['job_invol'],
                attrition=job['attrition'],
                registered_on=datetime.datetime.now()
            )
            save_changes(new_job)
    else:
        new_job = Job(
            id_account=account_id,
            name_inst=data['name_inst'],
            department=data['department'],
            job_level=data['job_level'],
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


def get_all_job():
    return Job.query.all()


def get_a_job(id_account):
    return Job.query.filter_by(id_account=id_account)


def save_changes(data):
    db.session.add(data)
    db.session.commit()

