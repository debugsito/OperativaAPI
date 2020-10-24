from app.main.model.account import Account
from ..service.blacklist_service import save_token
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from threading import Thread
import jwt

class Auth:

    @staticmethod
    def login_account(data):
        try:
            # fetch the Account data
            account = Account.query.filter_by(email=data.get('email')).first()
            if account and account.check_password(data.get('password')):
                auth_token = Account.encode_auth_token(account.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_account(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Account.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_account(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = Account.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                account = Account.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'account_id': account.id,
                        'email': account.email,
                        'registered_on': str(account.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

"""
	@staticmethod
	def reset_password(data):
		email=data.get('email')
		token = get_reset_token()
		msg = MIMEMultipart()
		message = "Code is: "+str(token)
		password = "your_password"
		msg['From'] = "your_address"
		msg['To'] = "to_address"
		msg['Subject'] = "Siminchik API Password Reset"
		msg.attach(MIMEText(message, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com: 587')
		server.starttls()
		server.login(msg['From'], password)
		server.sendmail(msg['From'], msg['To'], msg.as_string())
		server.quit()
		Thread(target=reset_password, args=(data)).start()
		return "successfully sent email to %s:" % (msg['To'])
	
	@staticmethod	
	def get_reset_token(self, expires=500):
		return jwt.encode({'reset_password': self.username,
			'exp':    time() + expires},
			key=os.getenv('SECRET_KEY_FLASK'))
			
	@staticmethod						   
	def verify_reset_token(token):
        try:
            email = jwt.decode(token,
              key=os.getenv('SECRET_KEY_FLASK'))['reset_password']
        except Exception as e:
            print(e)
            return
        return User.query.filter_by(email=email).first()
	"""