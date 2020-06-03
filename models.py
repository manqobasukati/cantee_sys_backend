

from datetime import date, datetime
from app import db



class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    user_surname = db.Column(db.String(100))



class Canteen(db.Model):
    __tablename__ = 'canteen'
    canteen_id = db.Column(db.Integer, primary_key=True)
    canteen_name = db.Column(db.String(100))


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    canteen_id = db.Column(db.Integer, db.ForeignKey('canteen.canteen_id'),
                               nullable=False)
    category = db.relationship('Canteen',
                               backref=db.backref('canteen', lazy=True))

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),
                               nullable=False)
    category = db.relationship('User',
                               backref=db.backref('user', lazy=True))





db.create_all()
