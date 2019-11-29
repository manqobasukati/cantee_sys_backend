from flask import Blueprint


api_print = Blueprint('api_print', __name__,url_prefix='/api/')

from application.api.api_user_login import *
from application.api.api_user_sign_up import *
from application.api.api_create_post import *
from application.api.api_view_all_posts import *
from application.api.api_handle_search import *



