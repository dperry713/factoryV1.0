from app.models import Product
from app.extensions import db

def get_paginated_products(page, per_page):
    paginated_result = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    products = [
        {"id": p.id, "name": p.name, "price": p.price}
        for p in paginated_result.items
    ]
    return {
        "products": products,
        "total": paginated_result.total,
        "pages": paginated_result.pages,
        "current_page": paginated_result.page,
        "per_page": paginated_result.per_page
    }

def get_all_products():
    products = Product.query.all()
    return [{"id": p.id, "name": p.name, "price": p.price} for p in products]

def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if product:
        return {"id": product.id, "name": product.name, "price": product.price}
    return None

def create_product(data):
    new_product = Product(name=data["name"], price=data["price"])
    db.session.add(new_product)
    db.session.commit()
    return {"id": new_product.id, "name": new_product.name, "price": new_product.price}

def update_product(product_id, data):
    product = Product.query.get(product_id)
    if product:
        product.name = data["name"]
        product.price = data["price"]
        db.session.commit()
        return {"id": product.id, "name": product.name, "price": product.price}
    return None

def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    return False
