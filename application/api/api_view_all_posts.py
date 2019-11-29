from application import db
from application import app
from application.api import api_print
from flask import render_template, jsonify, request
from application.models import User, Post, PostEvent
from application.api.api_user_login import token_required
from werkzeug.utils import secure_filename
import os



@api_print.route('/post', methods=['GET','PUT'])
@token_required
def get_posts(current_user):
	#from application.models import pos
	p = PostEvent.query.filter_by(user_id=current_user.user_id).all()
	print(p)
	posts = []	
	if request.method == 'GET':
		for i in p:
			post = {}
			post['post_event_id'] = i.id
			post['post_picture'] = i.post.post_picture
			post['post_message'] = i.post.post_message
			post['post_accepted'] = i.accepted
			posts.append(post)
	elif request.method == 'PUT':
		response = request.form
		pos = PostEvent.query.filter_by(id=response['post_event_id']).first()
		if response['post_accepted'] == 'true':
			files = request.files
			print(response)
			fi = files['post_ver_pic']
			filename = secure_filename(files['post_ver_pic'].filename)
			fi.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			pos.post_verification_pic = filename
			pos.accepted = True
			db.session.commit()
		else:
			pos.accepted = False
			db.session.commit()
		return jsonify({'message':'succesfully updated'})
	
	return jsonify(posts)


@api_print.route('/status', methods=['GET','PUT'])
@token_required
def get_statuses(current_user):
	#from application.models import pos
	p = PostEvent.query.filter(Post.post_user_id  == current_user.user_id).all()
	print(p)
	posts = []	
	if request.method == 'GET':
		for i in p:
			post = {}
			post['post_event_id'] = i.id
			post['post_verification_pic'] = i.post_verification_pic 
			post['post_message'] = i.post.post_message
			post['post_accepted'] = i.accepted
			posts.append(post)
	elif request.method == 'PUT':
		response = request.get_json(force=True)
		pos = PostEvent.query.filter_by(id=response["post_event_id"]).first()
		pos.post_verified = True
		db.session.commit()
		return jsonify({'message':'successfully verified post'})
	return jsonify(posts)
	



@api_print.route('/api/posts/<int:id>', methods=['GET','PUT','POST'])
def all_posts(id):
	return jsonify(id)

