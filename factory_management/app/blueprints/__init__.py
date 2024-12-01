from flask import Blueprint
from .employees import employees_bp
from .products import products_bp
from .orders import orders_bp
from .customers import customers_bp
from .production import production_bp

def register_blueprints(app):
    app.register_blueprint(employees_bp, url_prefix='/employees')
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(production_bp, url_prefix='/production')
