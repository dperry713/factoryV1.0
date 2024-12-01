from app.models import Customer
from app.extensions import db

def get_all_customers():
    customers = Customer.query.all()
    return [{"id": c.id, "name": c.name} for c in customers]

def get_customer_by_id(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        return {"id": customer.id, "name": customer.name}
    return None

def create_customer(data):
    new_customer = Customer(name=data["name"])
    db.session.add(new_customer)
    db.session.commit()
    return {"id": new_customer.id, "name": new_customer.name}

def update_customer(customer_id, data):
    customer = Customer.query.get(customer_id)
    if customer:
        customer.name = data["name"]
        db.session.commit()
        return {"id": customer.id, "name": customer.name}
    return None

def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return True
    return False
