from flask import request
from flask_restx import Resource

from ..util.dto import AttritionDto, Job_roleDto, DepartmentDto
from ..util.dto import Job_levelDto, FieldDto, LevelDto
from ..util.dto import DocumentDto, CivilDto
from ..service.ope_general_service import get_all_attrition
from ..service.ope_general_service import get_all_job_role
from ..service.ope_general_service import get_all_department
from ..service.ope_general_service import get_all_job_level
from ..service.ope_general_service import get_all_field
from ..service.ope_general_service import get_all_level
from ..service.ope_general_service import get_all_document
from ..service.ope_general_service import get_all_civil

api_AttritionDto = AttritionDto.api
_attrition = AttritionDto.attrition

api_Job_roleDto = Job_roleDto.api
_job_role = Job_roleDto.job_role

api_DepartmentDto = DepartmentDto.api
_department = DepartmentDto.department

api_Job_levelDto = Job_levelDto.api
_job_level = Job_levelDto.job_level

api_FieldDto = FieldDto.api
_field = FieldDto.field

api_LevelDto = LevelDto.api
_level = LevelDto.level

api_DocumentDto = DocumentDto.api
_document = DocumentDto.document

api_CivilDto = CivilDto.api
_civil = CivilDto.civil

@api_AttritionDto.route('/')
class AttritionList(Resource):
    @api_AttritionDto.doc('list_of_attrition')
    @api_AttritionDto.marshal_list_with(_attrition, envelope='data')
    def get(self):
        """List all attrition"""
        return get_all_attrition()
		

@api_Job_roleDto.route('/')
class Job_roleList(Resource):
    @api_Job_roleDto.doc('list_of_job_role')
    @api_Job_roleDto.marshal_list_with(_job_role, envelope='data')
    def get(self):
        """List all job_role"""
        return get_all_job_role()


@api_DepartmentDto.route('/')
class DepartmentList(Resource):
    @api_DepartmentDto.doc('list_of_department')
    @api_DepartmentDto.marshal_list_with(_department, envelope='data')
    def get(self):
        """List all department"""
        return get_all_department()
		
@api_Job_levelDto.route('/')
class Job_levelList(Resource):
    @api_Job_levelDto.doc('list_of_job_level')
    @api_Job_levelDto.marshal_list_with(_job_level, envelope='data')
    def get(self):
        """List all job_level"""
        return get_all_job_level()

@api_FieldDto.route('/')
class FieldList(Resource):
    @api_FieldDto.doc('list_of_field')
    @api_FieldDto.marshal_list_with(_field, envelope='data')
    def get(self):
        """List all field"""
        return get_all_field()
		
@api_LevelDto.route('/')
class LevelList(Resource):
    @api_LevelDto.doc('list_of_level')
    @api_LevelDto.marshal_list_with(_level, envelope='data')
    def get(self):
        """List all level"""
        return get_all_level()
		
@api_DocumentDto.route('/')
class DocumentList(Resource):
    @api_DocumentDto.doc('list_of_document')
    @api_DocumentDto.marshal_list_with(_document, envelope='data')
    def get(self):
        """List all document"""
        return get_all_document()
		
@api_CivilDto.route('/')
class CivilList(Resource):
    @api_CivilDto.doc('list_of_civil')
    @api_CivilDto.marshal_list_with(_civil, envelope='data')
    def get(self):
        """List all civil"""
        return get_all_civil()