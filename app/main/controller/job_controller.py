from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import JobDto
from ..service.job_service import save_new_job, get_all_job, get_a_job

api = JobDto.api
_job = JobDto.job


@api.route('/')
class JobList(Resource):
    @api.doc('list_of_registered_jobs')
    @api.marshal_list_with(_job, envelope='data')
    def get(self):
        """List all registered jobs"""
        return get_all_job()

    @api.expect(_job, validate=True)
    @api.response(201, 'Job successfully created.')
    @api.doc('create a new job')
    def post(self):
        """Creates a new Job """
        data = request.json
        return save_new_job(data=data)


@api.route('/<id_account>')
@api.param('id_account', 'The job identifier')
@api.response(404, 'Job not found.')
class Job(Resource):
    @api.doc('get a job')
    @api.marshal_with(_job)
    def get(self, id_account):
        """get a job given its identifier"""
        job = get_a_job(id_account)
        if not job:
            api.abort(404)
        else:
            return job



