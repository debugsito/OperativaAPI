from flask import request
from flask_restx import Resource

from ..util.dto import PublicationDto
from ..service.publication_service import save_new_publication, get_all_publication, get_a_publication

api = PublicationDto.api
_publication = PublicationDto.publication


@api.route('/')
class PublicationList(Resource):
    @api.doc('list_of_registered_publication')
    @api.marshal_list_with(_publication, envelope='data')
    def get(self):
        """List all registered publication"""
        return get_all_publication()

    @api.expect(_publication, validate=True)
    @api.response(201, 'Publication successfully created.')
    @api.doc('create a new publication')
    def post(self):
        """Creates a new publication """
        data = request.json
        return save_new_publication(data=data)


@api.route('/<id_enterprise>')
@api.param('id_enterprise', 'The Publication identifier')
@api.response(404, 'Publication not found.')
class Publication(Resource):
    @api.doc('get a publication')
    @api.marshal_with(_publication)
    def get(self, id_enterprise):
        """get a publication given its identifier"""
        publication = get_a_publication(id_enterprise)
        if not publication:
            api.abort(404)
        else:
            return publication



