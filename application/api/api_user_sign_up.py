from application import db
from application.api import api_print
from application.models import User
from flask import render_template, jsonify, request



@api_print.route('/user-registration', methods=['POST','GET'])
def user_registration_view():

	#Check to see if method is post, then get inputed fields
	if request.method == 'POST':
		content = request.get_json(force=True)
		user_name = content["user_name"]
		user_age = content["user_date_of_birth"]
		user_area_of_interest = content["user_area_of_interest"]
		user_surname = content["user_surname"]
		user_password = content["user_password"]
		user_phone_number = content["user_phone_number"]
		user_gender = content["user_gender"]
		if User.query.filter_by(user_phone_number = user_phone_number).first() is not None:
			return jsonify({'message':'user with phone number already exists'})
		if (user_name or user_surname or user_password or user_phone_number ) == None:
			return jsonify({'message':'missing data fields'})
		else:
			#First encrypt password 
			#user_password_hash = bcrypt.generate_password_hash(user_password)
			user = User(name=user_name,surname=user_surname,password=user_password,phone=user_phone_number,age= user_age, area_of_interest=user_area_of_interest,gender=user_gender)
			db.session.add(user)
			db.session.commit()
			return jsonify({'message':'succesfully registered'})
	


	



