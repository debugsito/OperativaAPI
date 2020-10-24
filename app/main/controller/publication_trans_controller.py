from flask import request
from flask_restx import Resource

from ..util.dto import Publication_transDto
from ..service.publication_trans_service import save_new_publication_trans, get_all_publication_trans, get_a_publication_trans

api = Publication_transDto.api
_publication_trans = Publication_transDto.publication_trans


@api.route('/')
class Publication_transList(Resource):
    @api.doc('list_of_registered_publication_trans')
    @api.marshal_list_with(_publication_trans, envelope='data')
    def get(self):
        """List all registered publication_trans"""
        return get_all_publication_trans()

    @api.expect(_publication_trans, validate=True)
    @api.response(201, 'Publication_trans successfully created.')
    @api.doc('create a new publication_trans')
    def post(self):
        """Creates a new publication_trans """
        data = request.json
        return save_new_publication_trans(data=data)


@api.route('/<id_publication>')
@api.param('id_publication', 'The Publication_trans identifier')
@api.response(404, 'Publication_trans not found.')
class Publication_trans(Resource):
    @api.doc('get a publication')
    @api.marshal_with(_publication_trans)
    def get(self, id_publication):
        """get a publication_trans given its identifier"""
        publication_trans = get_a_publication(id_publication)
        if not publication_trans:
            api.abort(404)
        else:
            return publication_trans



