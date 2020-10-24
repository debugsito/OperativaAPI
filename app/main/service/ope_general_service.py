import uuid
import datetime

from app.main import db
from app.main.model.document import Document
from app.main.model.civil import Civil
from app.main.model.level import Level
from app.main.model.field import Field
from app.main.model.department import Department
from app.main.model.job_level import Job_level
from app.main.model.job_role import Job_role
from app.main.model.attrition import Attrition

def get_all_document():
    return Document.query.all()

def get_all_civil():
    return Civil.query.all()	
	
def get_all_level():
	return Level.query.all()
	
def get_all_field():
	return Field.query.all()

def get_all_department():
	return Department.query.all()

def get_all_job_level():
	return Job_level.query.all()

def get_all_job_role():
	return Job_role.query.all()

def get_all_attrition():
	return Attrition.query.all()