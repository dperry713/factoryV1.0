from app.models import Order
from app.extensions import db

def get_paginated_orders(page, per_page):
    paginated_result = Order.query.paginate(page=page, per_page=per_page, error_out=False)
    orders = [
        {"id": o.id, "product_id": o.product_id, "customer_id": o.customer_id, "quantity": o.quantity}
        for o in paginated_result.items
    ]
    return {
        "orders": orders,
        "total": paginated_result.total,
        "pages": paginated_result.pages,
        "current_page": paginated_result.page,
        "per_page": paginated_result.per_page
    }

def get_all_orders():
    orders = Order.query.all()
    return [
        {"id": o.id, "product_id": o.product_id, "customer_id": o.customer_id, "quantity": o.quantity}
        for o in orders
    ]

def get_order_by_id(order_id):
    order = Order.query.get(order_id)
    if order:
        return {"id": order.id, "product_id": order.product_id, "customer_id": order.customer_id, "quantity": order.quantity}
    return None

def create_order(data):
    new_order = Order(product_id=data["product_id"], customer_id=data["customer_id"], quantity=data["quantity"])
    db.session.add(new_order)
    db.session.commit()
    return {"id": new_order.id, "product_id": new_order.product_id, "customer_id": new_order.customer_id, "quantity": new_order.quantity}

def update_order(order_id, data):
    order = Order.query.get(order_id)
    if order:
        order.product_id = data["product_id"]
        order.customer_id = data["customer_id"]
        order.quantity = data["quantity"]
        db.session.commit()
        return {"id": order.id, "product_id": order.product_id, "customer_id": order.customer_id, "quantity": order.quantity}
    return None

def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return True
    return False
