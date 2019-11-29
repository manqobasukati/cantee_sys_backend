import  re
from application import db, bcrypt
from datetime import date, datetime


class User(db.Model):
	__tablename__ = 'users'
	user_id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(100))
	user_surname = db.Column(db.String(100))
	user_phone_number = db.Column(db.String(10))
	user_password = db.Column(db.String(1000))
	user_age = db.Column(db.String(20))
	user_gender = db.Column(db.String(10))
	user_area_of_interest = db.Column(db.String(20))
	
	def __init__(self,name,surname,password,phone,age, area_of_interest,gender):
		self.user_password = bcrypt.generate_password_hash(password).decode('utf-8')
		self.user_phone_number =  phone	
		self.user_name = name
		self.user_surname = surname
		self.user_age = self.calculateAge(age)
		self.user_area_of_interest = area_of_interest
		self.user_gender = gender
		
		
	def calculateAge(self,bd): 
		birthDate = datetime.strptime(bd, '%Y-%m-%d')
		today = date.today() 
		age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
		return age 
		
		

		
class Post(db.Model):
	__tablename__ = 'posts'
	post_id = db.Column(db.Integer, primary_key=True)
	post_area = db.Column(db.String(100))
	post_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	user = db.relationship('User', backref='user', uselist=False)
	post_no_of_days = db.Column(db.Integer)
	post_picture = db.Column(db.String(100))
	post_message = db.Column(db.String(100))
	
	
	
class PostEvent(db.Model):
	__tablename__ = 'post_events'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	user = db.relationship('User', backref='poster', uselist=False)
	post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))
	post = db.relationship('Post', backref='post', uselist=False)
	accepted = db.Column(db.Boolean)
	post_verified = db.Column(db.Boolean)
	post_verification_pic = db.Column(db.String(100))










	
	
	
	
		
	


	
	
	
	
	
	
	

	
	
db.create_all()