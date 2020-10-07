from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.locate_controller import api_CountryDto, api_CityDto, api_StateDto

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Operativa API',
          version='1.0',
          description='Opetaiva API brinda servicio de monitario de clientes y empresas.'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(api_CountryDto, path='/country')
api.add_namespace(api_StateDto, path='/state')
api.add_namespace(api_CityDto, path='/city')
