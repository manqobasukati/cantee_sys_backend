from flask import Flask
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

bcrypt = Bcrypt()

admin = Admin()

app = Flask(__name__, instance_relative_config=False)


def create_app():
	#app = Flask(__name__, instance_relative_config=False)
	cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
	app.config.from_object('config.DevelopmentConfig')
	app.config['CORS_HEADERS'] = 'Content-Type'
	
	db.init_app(app)
	admin.init_app(app)
	bcrypt.init_app(app)
	
	with app.app_context():
		from application.api import api_print
		from application.admin import UserAdmin, PostAdmin, PostEventAdmin
		
		app.register_blueprint(api_print)
		
		return app
		
		
		
	