from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import EducationDto
from ..service.education_service import save_new_education, get_all_education, get_a_education

api = EducationDto.api
_education = EducationDto.education


@api.route('/')
class EducationList(Resource):
    @api.doc('list_of_registered_educations')
    @api.marshal_list_with(_education, envelope='data')
    def get(self):
        """List all registered educations"""
        return get_all_education()

    @api.expect(_education, validate=True)
    @api.response(201, 'Education successfully created.')
    @api.doc('create a new education')
    def post(self):
        """Creates a new Education """
        data = request.json
        return save_new_education(data=data)


@api.route('/<id_account>')
@api.param('id_account', 'The Education identifier')
@api.response(404, 'Education not found.')
class Education(Resource):
    @api.doc('get an education')
    @api.marshal_with(_education)
    def get(self, id_account):
        """get an education given its identifier"""
        education = get_a_education(id_account)
        if not education:
            api.abort(404)
        else:
            return education



