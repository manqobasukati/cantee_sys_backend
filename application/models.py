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
	user = db.relationship('User', backref='person_making_post', uselist=False)
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
	start_time = db.Column(db.Integer)
	stop_time = db.Column(db.Integer)
	date = db.Column(db.String(100))
	

	def calculateDuration(self):
		duration = self.stop_time - self.start_time
		return duration


class PostVerificationPictures(db.Model):
	__tablename__ = 'post_verification_pictures'
	id = db.Column(db.Integer, primary_key=True)
	post_event_id = db.Column(db.Integer, db.ForeignKey('post_events.id'))
	post_event = db.relationship('PostEvent',backref='post_event',uselist=False)
	post_is_ver_1 = db.Column(db.Boolean)
	post_is_ver_2 = db.Column(db.Boolean)
	post_verif_pic_1 = db.Column(db.String(100))
	post_verif_pic_2 = db.Column(db.String(100))
	











	
	
	
	
		
	


	
	
	
	
	
	
	

	
	
db.create_all()