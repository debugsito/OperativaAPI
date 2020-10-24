from flask_restx import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns
from .main.controller.account_controller import api as account_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.education_controller import api as edu_ns
from .main.controller.job_controller import api as job_ns
from .main.controller.locate_controller import api_CountryDto  
from .main.controller.locate_controller import api_CityDto
from .main.controller.locate_controller import api_StateDto
from .main.controller.ope_general_controller import api_AttritionDto
from .main.controller.ope_general_controller import api_Job_roleDto
from .main.controller.ope_general_controller import api_DepartmentDto
from .main.controller.ope_general_controller import api_Job_levelDto
from .main.controller.ope_general_controller import api_FieldDto
from .main.controller.ope_general_controller import api_LevelDto
from .main.controller.ope_general_controller import api_DocumentDto
from .main.controller.ope_general_controller import api_CivilDto
from .main.controller.enterprise_controller import api as ent_ns
from .main.controller.publication_controller import api as pub_ns
from .main.controller.publication_trans_controller import api as pub_trans_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Operativa API',
          version='1.0',
          description='Opetaiva API brinda servicio de monitario de clientes y empresas.'
          )

api.add_namespace(auth_ns)
api.add_namespace(account_ns, path='/account')
api.add_namespace(user_ns, path='/user')
api.add_namespace(edu_ns, path='/education')
api.add_namespace(job_ns, path='/job')
api.add_namespace(api_CountryDto, path='/country')
api.add_namespace(api_StateDto, path='/state')
api.add_namespace(api_CityDto, path='/city')
api.add_namespace(api_AttritionDto, path='/attrition')
api.add_namespace(api_Job_roleDto, path='/job_role')
api.add_namespace(api_DepartmentDto, path='/department')
api.add_namespace(api_Job_levelDto, path='/job_level')
api.add_namespace(api_FieldDto, path='/field')
api.add_namespace(api_LevelDto, path='/level')
api.add_namespace(api_DocumentDto, path='/document')
api.add_namespace(api_CivilDto, path='/civil')
api.add_namespace(ent_ns, path='/enterprise')
api.add_namespace(pub_ns, path='/publication')
api.add_namespace(pub_trans_ns, path='/publication_trans')