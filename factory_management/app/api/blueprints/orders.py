from flask import Blueprint, request, jsonify
from app.services.order_service import (
    get_all_orders,
    get_order_by_id,
    create_order,
    update_order,
    delete_order,
)
import get_paginated_orders

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['GET'])
def list_orders():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    paginated_orders = get_paginated_orders(page, per_page)
    return jsonify(paginated_orders), 200

@orders_bp.route('/', methods=['GET'])
def list_orders():
    orders = get_all_orders()
    return jsonify(orders), 200

@orders_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = get_order_by_id(order_id)
    if order:
        return jsonify(order), 200
    return jsonify({"error": "Order not found"}), 404

@orders_bp.route('/', methods=['POST'])
def add_order():
    data = request.json
    new_order = create_order(data)
    return jsonify(new_order), 201

@orders_bp.route('/<int:order_id>', methods=['PUT'])
def modify_order(order_id):
    data = request.json
    updated_order = update_order(order_id, data)
    if updated_order:
        return jsonify(updated_order), 200
    return jsonify({"error": "Order not found"}), 404

@orders_bp.route('/<int:order_id>', methods=['DELETE'])
def remove_order(order_id):
    if delete_order(order_id):
        return jsonify({"message": "Order deleted"}), 200
    return jsonify({"error": "Order not found"}), 404
