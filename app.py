
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import request




app = Flask(__name__)
db = SQLAlchemy(app)
admin = Admin(app)


from models import User, Canteen, Order






@app.route("/users/<int:user_id>/order", methods=["POST"])
def user_orders(user_id):
    user = User.query.filter_by(user_id= user_id).first()
    if user:
        order = Order.query.filter_by(user_id = user_id).all()

    return "User views all orders"


@app.route("/users/<int:user_id>/order/<int:order_id>", methods=["GET"])
def user_specific_order():
    user = User.query.filter_by(user_id= user_id).first()
    if user:
        order = Order.query.filter_by(order_id = order_id,user_id=user_id).first()
        if order:
            respone = dict()
            respone["user_id"] = user.id
            respone["status"] = order.status
            respone["order_id"] = order.id
            return jsonify(respone)
    return "user tracks specific order"

@app.route("/canteen/<int:canteen_id>/orders", methods=["GET"])
def view_canteen_orders(canteen_id):
    orders = Order.query.filter_by(canteen_id=canteen_id).all()
    if orders:
        canteen_orders = []
        for order in orders:
            ord =dict()
            ord["order_id"] = order.id
            ord["order_satus"] =order.status
            canteen_orders.append(ord)

        return jsonify({'response':canteen_orders})
    return jsonify({"response":"no orders"})

@app.route("/canteen/<int:canteen_id>/orders", methods=["POST"])
def create_order(canteen_id):
    data = request.data
    if data:
        user  = User.query.filter_by(user_id=data.user_id).first()
        canteen =  Canteen.query.filter_by(canteen_id=data.canteen_id).first()
        order = Order(user_id=data.user_id,user=user,canteen=canteen,canteen_id=canteen_id)
        if order:
            db.session.add(order)
            db.session.commit()
            return jsonify({"repsonse":"order_created"})
    else:
        return jsonify({"repsonse":"Pleas provide data"})
    return "create order"

@app.route("/canteen/<int:canteen_id>/menu",methods=["GET"])
def view_canteen_menu():
    return "canteen menu"

@app.route("/canteen/<int:canteen_id>/menu", methods=['POST'])
def create_canteen_menu():
    return "canteen menu"




admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Canteen, db.session))
admin.add_view(ModelView(Order, dbs.session))

if __name__ == "__main__":
    # app.run(str(IPAddr))
     app.run(host='127.0.0.1', debug=True)
