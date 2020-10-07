from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')})#,
	#	'first_name': fields.String(required=True, description='user first_name'),
        #'middle_name': fields.String(required=True, description='user middle_name'),
	#	'last_name': fields.String(required=True, description='user last_name'),
        #'type_doc': fields.Integer(required=True, description='user type_doc'),
	#	'num_doc': fields.String(required=True, description='user num_doc'),
        #'id_country': fields.Integer(required=True, description='user id_country'),
	#	'id_state': fields.Integer(required=True, description='user id_state'),
        #'id_city': fields.Integer(required=True, description='user id_city'),
	#	'registered_on': fields.DateTime(required=True, description='user registered_on')
   # })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password ')
    })

class CountryDto:
    api = Namespace('country', description='country related operations')
    country = api.model('country', {
		'id': fields.Integer(required=True, description='The id of the country'),
        'sort_name': fields.String(required=True, description='The sort name of the country'),
        'name': fields.String(required=True, description='The name of the country'),
		'phone_code': fields.Integer(required=True, description='The phone code of the country')
    })
	
class StateDto:
    api = Namespace('state', description='state related operations')
    state = api.model('state', {
		'id': fields.Integer(required=True, description='The id of the state'),
        'name': fields.String(required=True, description='The name of the state'),
		'id_country': fields.Integer(required=True, description='The id_country of the country')
    })	
	
	
class CityDto:
    api = Namespace('city', description='city related operations')
    city = api.model('city', {
        'name': fields.String(required=True, description='The name of the city'),
		'id_state': fields.Integer(required=True, description='The id_state of the state')
    })
