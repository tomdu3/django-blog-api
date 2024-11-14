import jwt
import random
import string
from django.conf import settings
from datetime import datetime, timedelta
from .models import CustomAuth

def get_random_string(length=6):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_access_token(payload):
	return jwt.encode({'exp': datetime.now() + timedelta(minutes=60), **payload}, settings.SECRET_KEY, algorithm='HS256')

def get_refresh_token():
	return jwt.encode({'exp': datetime.now() + timedelta(days=7), 'data': get_random_string(10)}, settings.SECRET_KEY, algorithm='HS256')

def verify_token(token):
	try:
		data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
	except jwt.ExpiredSignatureError:
		return None
	exp = data['exp']
	if datetime.now().timestamp() > exp:
		return None
	return data

def decode_jwt(bearer):
	if not bearer:
		return None
	token = bearer[7:]
	data = verify_token(token)
	if data:
		try:
			return CustomAuth.objects.get(id=data['user_id'])
		except Exception:
			return None
