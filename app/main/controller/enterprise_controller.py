from flask import request
from flask_restx import Resource

from ..util.dto import EnterpriseDto
from ..service.enterprise_service import save_new_enterprise, get_all_enterprise, get_a_enterprise

api = EnterpriseDto.api
_enterprise = EnterpriseDto.enterprise


@api.route('/')
class EnterpriseList(Resource):
    @api.doc('list_of_registered_enterprise')
    @api.marshal_list_with(_enterprise, envelope='data')
    def get(self):
        """List all registered enterprise"""
        return get_all_enterprise()

    @api.expect(_enterprise, validate=True)
    @api.response(201, 'Enterprise successfully created.')
    @api.doc('create a new enterprise')
    def post(self):
        """Creates a new Enterprise """
        data = request.json
        return save_new_enterprise(data=data)


@api.route('/<id_account>')
@api.param('id_account', 'The Enterprise identifier')
@api.response(404, 'Enterprise not found.')
class Enterprise(Resource):
    @api.doc('get a Enterprise')
    @api.marshal_with(_enterprise)
    def get(self, id_account):
        """get a enterprise given its identifier"""
        enterprise = get_a_enterprise(id_account)
        if not enterprise:
            api.abort(404)
        else:
            return enterprise



