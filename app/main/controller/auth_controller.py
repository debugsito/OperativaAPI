from flask import request
from flask_restx import Resource


from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
account_auth = AuthDto.account_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('Account login')
    @api.expect(account_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_account(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout an account')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_account(data=auth_header)

		
@api.route('/reset_password')
class RestPasswordAPI(Resource):
    """
    Reset Password Resource
    """
    @api.doc('reset passowrd')
    def post(self):
        
        return 'Sent'		

