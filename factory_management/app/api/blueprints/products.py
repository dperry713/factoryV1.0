from flask import Blueprint, request, jsonify
from app.services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
)
import get_paginated_products

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def list_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    paginated_products = get_paginated_products(page, per_page)
    return jsonify(paginated_products), 200

@products_bp.route('/', methods=['GET'])
def list_products():
    products = get_all_products()
    return jsonify(products), 200

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

@products_bp.route('/', methods=['POST'])
def add_product():
    data = request.json
    new_product = create_product(data)
    return jsonify(new_product), 201

@products_bp.route('/<int:product_id>', methods=['PUT'])
def modify_product(product_id):
    data = request.json
    updated_product = update_product(product_id, data)
    if updated_product:
        return jsonify(updated_product), 200
    return jsonify({"error": "Product not found"}), 404

@products_bp.route('/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    if delete_product(product_id):
        return jsonify({"message": "Product deleted"}), 200
    return jsonify({"error": "Product not found"}), 404
