from flask_restx import Namespace, fields

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    account_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password ')
    })


class AccountDto:
    api = Namespace('account', description='account related operations')
    account = api.model('account', {
        'email': fields.String(required=True, description='account email address'),
        'password': fields.String(required=True, description='account password'),
		'term_condi': fields.Integer(required=True, description='terms of data conditions')
		})

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id_account': fields.Integer(required=True, description='Id account'),
		'first_name': fields.String(required=True, description='user first_name'),
		'last_name': fields.String(required=True, description='user last_name'),
		'gender': fields.Integer(required=True, description='gender'),
        'type_doc': fields.Integer(required=True, description='user type_doc'),
		'num_doc': fields.String(required=True, description='user num_doc'),
		'birth_date': fields.String(required=True, description='birth_date'),
		'address': fields.String(required=True, description='address'),
		'phone': fields.String(required=True, description='phone'),
        'id_country': fields.Integer(required=True, description='user id_country'),
		'id_state': fields.Integer(required=True, description='user id_state'),
        'id_city': fields.Integer(required=True, description='user id_city'),
		'id_civil_status': fields.Integer(required=True, description='id_civil_status'),
		'id_provider': fields.Integer(required=True, description='id_provider')
    })

class EducationDto:
    api = Namespace('education', description='education related operations')
    education = api.model('education', {
        'id_account': fields.Integer(required=True, description='Id account'),
		'level': fields.Integer(required=True, description='level'),
		'name_inst': fields.String(required=True, description='name_inst'),
		'field': fields.Integer(required=True, description='field'),
        'from_year': fields.String(required=True, description='from_year'),
		'to_year': fields.String(required=True, description='to_year')
    })	

class JobDto:
    api = Namespace('job', description='job related operations')
    job = api.model('job', {
        'id_account': fields.Integer(required=True, description='Id account'),
		'name_inst': fields.String(required=True, description='name_inst'),
		'department': fields.Integer(required=True, description='department'),
		'job_level': fields.Integer(required=True, description='job_level'),
        'from_year': fields.String(required=True, description='from_year'),
		'to_year': fields.String(required=True, description='to_year'),
		'buss_travel': fields.Integer(required=True, description='buss_travel'),
		'distan_home': fields.Float(required=True, description='distan_home'),
		'hour_rate': fields.Float(required=True, description='hour_rate'),
        'job_role': fields.Integer(required=True, description='job_role'),
		'job_sati': fields.Integer(required=True, description='job_sati'),
        'monthly_income': fields.Float(required=True, description='monthly_income'),
		'over_time': fields.Integer(required=True, description='over_time'),
		'work_bal_life': fields.Integer(required=True, description='work_bal_life'),
		'job_invol': fields.Integer(required=True, description='job_invol'),
		'attrition': fields.Integer(required=True, description='attrition')
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

class AttritionDto:
    api = Namespace('attrition', description='attrition related operations')
    attrition = api.model('attrition', {
		'id': fields.Integer(required=True, description='The id of the state'),
        'name': fields.String(required=True, description='The name of'),
		'description': fields.String(required=True, description='The description of the state')
    })
	
class Job_roleDto:
    api = Namespace('job_role', description='job_role related operations')
    job_role = api.model('job_role', {
		'id': fields.Integer(required=True, description='The id of the state'),
        'name': fields.String(required=True, description='The name of'),
		'description': fields.String(required=True, description='The description of the state')
    })
	
class DepartmentDto:
    api = Namespace('department', description='department related operations')
    department = api.model('department', {
		'id': fields.Integer(required=True, description='The id of the state'),
        'name': fields.String(required=True, description='The name of'),
		'description': fields.String(required=True, description='The description of the state')
    })
	
class Job_levelDto:
    api = Namespace('job_level', description='job_level related operations')
    job_level = api.model('job_level', {
		'id': fields.Integer(required=True, description='The id of the state'),
        'name': fields.String(required=True, description='The name of'),
		'description': fields.String(required=True, description='The description of the state')
    })
	
class FieldDto:
    api = Namespace('field', description='field related operations')
    field = api.model('field', {
		'id': fields.Integer(required=True, description='The id of the state'),
        'name': fields.String(required=True, description='The name of'),
		'description': fields.String(required=True, description='The description of the state')
    })
	
class LevelDto:
    api = Namespace('level', description='level related operations')
    level = api.model('level', {
		'id': fields.Integer(required=True, description='The id of the state'),
        'name': fields.String(required=True, description='The name of'),
		'description': fields.String(required=True, description='The description of the state')
    })
	
class DocumentDto:
    api = Namespace('document', description='document related operations')
    document = api.model('document', {
		'id': fields.Integer(required=True, description='The id of the state'),
        'name': fields.String(required=True, description='The name of'),
		'description': fields.String(required=True, description='The description of the state')
    })
	
class CivilDto:
    api = Namespace('civil', description='civil related operations')
    civil = api.model('civil', {
		'id': fields.Integer(required=True, description='The id of the state'),
        'name': fields.String(required=True, description='The name of'),
		'description': fields.String(required=True, description='The description of the state')
    })
	
class EnterpriseDto:
    api = Namespace('enterprise', description='enterprise related operations')
    enterprise = api.model('enterprise', {
        'id_account': fields.Integer(required=True, description='Id account'),
		'name': fields.String(required=True, description='name'),
		'ruc': fields.String(required=True, description='ruc'),
		'address': fields.Integer(required=True, description='address'),
        'phone': fields.Integer(required=True, description='phone'),
		'fax': fields.String(required=True, description='fax'),
		'type_job': fields.Integer(required=True, description='type_job')
    })
	
class PublicationDto:
    api = Namespace('publication', description='publication related operations')
    publication = api.model('publication', {
        'id_enterprise': fields.Integer(required=True, description='id_enterprise'),
		'description': fields.String(required=True, description='description'),
		'from_date': fields.String(required=True, description='from_date'),
		'to_date': fields.String(required=True, description='to_date'),
        'job_role': fields.Integer(required=True, description='job_role'),
		'type_job': fields.Integer(required=True, description='type_job'),
		'salary': fields.Integer(required=True, description='salary'),
		'url': fields.Integer(required=True, description='url')
    })
	
class Publication_transDto:
    api = Namespace('publication_trans', description='publication_trans related operations')
    publication_trans = api.model('publication_trans', {
        'id_publication': fields.Integer(required=True, description='id_publication'),
		'id_user': fields.Integer(required=True, description='id_user'),
		'description': fields.String(required=True, description='description')
    })