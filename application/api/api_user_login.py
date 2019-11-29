from application.api import api_print
from flask_cors import cross_origin
from flask import render_template, jsonify, request
import jwt
import datetime
from functools import wraps 
from application import db, bcrypt,app
from application.models import User




def token_required(f):
	
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		
		if 'x-access-token' in request.headers :
			token = request.headers['x-access-token']
			
		
			
		if not token:
			return jsonify({'message':'Token is missing!'}),401
			
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
			print(data)
			current_user = User.query.filter_by(user_id=data['user_id']).first()
		except:
			return jsonify({'message':'Token is invalid!'}), 401
			
	
		return f(current_user, *args, **kwargs)
		
	return decorated
	
	


@api_print.route("/user-login", methods=['GET','POST'])
def user_login_view():
	auth  = request.json
	#print(auth)
	if not auth or not auth['user_phone_number'] or not auth['user_password']:
		#return make_response('Could not verify 1', 401,{'WWW-Authenticate':'Basic realm="Login required!"'})
		return jsonify({'message':'mobile number and password were not provided'})
	#print(auth['user_phone_number'])
	user = User.query.filter_by(user_phone_number = auth['user_phone_number']).first()
	#print(auth.username)
	if not user:
		#make_response('Could not verify 2', 401,{'WWW-Authenticate':'Basic realm="Login required!"'})
		return jsonify({'message':'user does not exist'})
		
	
	if bcrypt.check_password_hash(user.user_password, auth['user_password']):
		token = jwt.encode({'user_id':user.user_id,'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
		return jsonify({'token': token.decode('UTF-8'),'user_name':user.user_name,
				'user_surname':user.user_surname,'user_phone_number':user.user_phone_number,
				'message':'success','user_id':user.user_id})
	else:
		return jsonify({'message': 'passowrd is incorrect'})

	
	return make_response('Could not verify 3', 401,{'WWW-Authenticate':'Basic realm="Login required!"'})
	