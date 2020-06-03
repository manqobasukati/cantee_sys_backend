from application import db
from application import app
from application.api import api_print
from application.api.api_user_login import token_required
from flask import render_template, jsonify, request
from application.models import User, Post, PostEvent
from flask import render_template, jsonify, request
from werkzeug.utils import secure_filename
from inspect import currentframe
import os



@api_print.route('/create-post', methods=['POST'])
@token_required
def create_post_view(current_user):
	content =  request.form
	files = request.files
	if request.method == 'POST':
		post_days = content['post_days']
		post = Post(post_no_of_days=post_days)
		fi = files['post_picture']
		filename = secure_filename(files['post_picture'].filename)
		fi.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		post.post_picture  = filename
		post.post_message = content['post_message']
		post.post_user_id = current_user.user_id
		post.post_area = content['post_area']
		post.user = current_user
		db.session.add(post)
		db.session.commit()

		for i in content['requested_users']:
			if i is not ',':
				post_event = PostEvent()
				post_event.user_id = int(i)
				post_event.post_id = post.post_id
				post_event.accepted = False
				post_event.start_time = content['post_start_time']
				post_event.stop_time = content['post_end_time']
				db.session.add(post_event)
				db.session.commit()
		return jsonify({'message':'created post'})	
		
		
	return jsonify({'message':'post not created'})


