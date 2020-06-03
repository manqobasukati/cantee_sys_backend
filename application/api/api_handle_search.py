from application import db
from application.api import api_print
from application.api.api_user_login import token_required

from flask import render_template, jsonify, request
from application.models import User, Post, PostEvent
from flask import render_template, jsonify, request

from application.api.utility_functions import return_as_dict







@api_print.route('/search-users',methods=['GET','POST'])
def search_users():
	content = request.get_json(force=True)

	
	if request.method == 'POST':
		found_users = User.query.filter((User.user_age >= content['user_age_from']) &
											(User.user_age <= content['user_age_to']) &
												(User.user_area_of_interest == content['user_area_of_interest'])&
													(User.user_gender == content['user_gender'])).all()

								
		if found_users:	
			users = []
			for user in found_users:
				user_as_dict = return_as_dict(user)
				users.append(user_as_dict)
			return jsonify({'message':users})
		else:
			return jsonify({'message':'no found users'})
		
	return jsonify({'message':'You should not be here'})

