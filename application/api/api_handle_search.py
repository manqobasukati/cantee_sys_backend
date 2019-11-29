from application import db
from application.api import api_print
from application.api.api_user_login import token_required
from flask import render_template, jsonify, request
from application.models import User, Post, PostEvent
from flask import render_template, jsonify, request


@api_print.route('/search-users',methods=['GET','POST'])
def search_users():
	content = request.get_json(force=True)
	print(content)
	if request.method == 'POST':
		found_users = User.query.filter((User.user_age >= content['user_age_from']) &
											(User.user_age <= content['user_age_to']) &
												(User.user_area_of_interest == content['user_area_of_interest'])&
													(User.user_gender == content['user_gender'])).all()
		if found_users:	
			users = []
			for i in found_users:
				user = {}
				user['user_id'] = i.user_id
				user['user_name'] = i.user_name
				user['user_surname'] = i.user_surname
				user['user_phone_number'] = i.user_phone_number
				user['user_age'] =  i.user_age
				user['user_gender'] = i.user_gender
				user['user_area_of_interest'] = i.user_area_of_interest
				users.append(user)
				
			return jsonify({'message':users})
		else:
			return jsonify({'message':'no found users'})
		
	return jsonify({'message':'You should not be here'})

