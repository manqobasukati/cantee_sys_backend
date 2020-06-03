
# Flask and Flask-SQLAlchemy initialization here
from flask_admin.contrib.sqla import ModelView
from app import admin
from models import User, Canteen, Order

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Canteen, db.session))
admin.add_view(ModelView(Order, dbs.session))