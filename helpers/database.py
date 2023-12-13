from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Order(Base):
    __tablename__ = 'order_table'

    id = Column(Integer, primary_key=True)
    users_id = Column(String(100), primary_key=False, nullable=False)
    product_code = Column(String(100), nullable=False)
    customer_fullname = Column(String(100), nullable=False)
    product_name = Column(String(100), nullable=False)
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def json(self):
        return {'id': self.id, 'users_id': self.users_id, 'product_code': self.product_code, 
                'customer_fullname': self.customer_fullname, 'product_name': self.product_name, 
                'total_amount': self.total_amount, 'created_at': self.created_at}
        

def get_order(data, session):
  try:
    ca = data['created_at']
    uid = data['users_id']
    order_query = session.query(Order)
    order = order_query.filter(Order.created_at==ca, Order.users_id==uid).first()
    if order:
      return order.id
  except Exception as e:
    return f"failed with exception {e}"