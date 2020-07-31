from flask import request
from flask_restx import Resource
import os

from app.main.util.decorator import admin_token_required
from ..util.dto import TranscriptionDto
from ..service.transcription_service import save_new_transcription, allowed_file, createFile
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

api = TranscriptionDto.api
_transcription = TranscriptionDto.transcription

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)


UPLOAD_FOLDER = '/home/rodolfo/SiminchikAPI/audio'

@api.route('/')
@api.expect(upload_parser)
class Upload(Resource):
	@api.response(201, 'Transcription successfully created.')
	@api.doc('Transcription an audio')
	def post(self):
		args = upload_parser.parse_args()
		uploaded_file = args['file']
		file = uploaded_file
		print (file.filename)
		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			date = createFile()
			url = UPLOAD_FOLDER+"/"+date
			if not os.path.exists(url):
				os.makedirs(url)
			file.save(os.path.join(url, filename))
			return save_new_transcription(file.filename,url)