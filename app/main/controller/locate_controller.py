from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import CountryDto, CityDto, StateDto
from ..service.locate_service import get_all_contries, get_all_states, get_all_cities

api_CountryDto = CountryDto.api
_country = CountryDto.country

api_StateDto = StateDto.api
_state = StateDto.state

api_CityDto = CityDto.api
_city = CityDto.city

@api_CountryDto.route('/')
class CountryList(Resource):
    @api_CountryDto.doc('list_of_countries')
    @api_CountryDto.marshal_list_with(_country, envelope='data')
    def get(self):
        """List all countries"""
        return get_all_contries()
		

@api_StateDto.route('/')
class CountryList(Resource):
    @api_StateDto.doc('list_of_states')
    @api_StateDto.marshal_list_with(_state, envelope='data')
    def get(self):
        """List all states"""
        return get_all_states()


@api_CityDto.route('/')
class CountryList(Resource):
    @api_CityDto.doc('list_of_city')
    @api_CityDto.marshal_list_with(_city, envelope='data')
    def get(self):
        """List all cities"""
        return get_all_cities()