from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
from datetime import datetime
from helpers.rabbitmq import use_rabbitmq
from helpers.asyncio import fetch_data
from helpers.database import Order, Base, get_order


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

app.app_context().push()

with app.app_context():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.commit()

#during development, to verify service is running
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'tester route'}), 200)


@app.route('/add_order_to_db', methods=['POST'])
def add_order_to_db(data):
  try:
    new_order = Order(
                      users_id=data['users_id'], 
                      product_code=data['product_code'],
                      customer_fullname=data['customer_fullname'],
                      product_name=data['product_name'],
                      total_amount=data['total_amount'],
                      created_at=data['created_at']
                      )
    db.session.add(new_order)
    db.session.commit()
    return make_response(jsonify({'message': 'order created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': f'error creating order, {e}'}), 500)


@app.route('/orders', methods=['POST'])
async def place_order():
  try:
    data = request.get_json()
    
    users_id=data['users_id']
    user_url=environ.get('USER_SERVICE_URL')
    user_info = await fetch_data(user_url, users_id)
    
    product_code=data['product_code']
    product_url=environ.get('PRODUCT_SERVICE_URL')
    product_info = await fetch_data(product_url, product_code)
    
    product_name = product_info['name']
    price = product_info['price']
    customer_name = f'{user_info["firstName"]} {user_info["lastName"]}'
    created_at = str(datetime.now())
    
    order_table_entry = {
      "users_id": users_id,
      "product_code": product_code,
      "customer_fullname": customer_name,
      "product_name": product_name,
      "total_amount": price,
      "created_at": created_at
    }
    
    add_order_to_db(order_table_entry)

    order_id = get_order(order_table_entry, db.session)
    
    rabbitmq_payload = {
      "order_id": order_id,
      "customer_fullname": customer_name,
      "product_name": product_name,
      "total_amount": price,
      "created_at": created_at
    }
    rabbitmq_details = {
      "user": environ.get("RABBITMQ_DEFAULT_USER"),
      "pass": environ.get("RABBITMQ_DEFAULT_PASS"),
      "host": "rabbitmq",
      "queue": "created_order",
      "exchange": "orders",
      "payload": rabbitmq_payload
    }
    
    use_rabbitmq(rabbitmq_details)
    
    return make_response(jsonify({'message': f'added the following order: id is {order_id} and entry is {order_table_entry}'}), 201)
  
  except Exception as e:
    return make_response(jsonify({'message': f'error creating order, {e}'}), 500)

