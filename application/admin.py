from flask_admin.contrib.sqla import ModelView
from application import db,admin
from application.models import User, Post, PostEvent

class PostView(ModelView):
    list_columns = ['post_id','post_area','post_picture',
                    'post_message','post_user_id']

class PostEventView(ModelView):
    list_columns = ['post_id','id','accepted','post_verified',
                    'post_verification_pic','user_id','user.user_name','start_time','stop_time','date']



UserAdmin = admin.add_view(ModelView(User, db.session))
PostAdmin = admin.add_view(PostView(Post, db.session))
PostEventAdmin = admin.add_view(PostEventView(PostEvent, db.session))
