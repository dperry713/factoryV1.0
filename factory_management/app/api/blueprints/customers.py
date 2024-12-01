from flask import Blueprint, request, jsonify
from app.services.customer_service import (
    get_all_customers,
    get_customer_by_id,
    create_customer,
    update_customer,
    delete_customer,
)

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/', methods=['GET'])
def list_customers():
    customers = get_all_customers()
    return jsonify(customers), 200

@customers_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = get_customer_by_id(customer_id)
    if customer:
        return jsonify(customer), 200
    return jsonify({"error": "Customer not found"}), 404

@customers_bp.route('/', methods=['POST'])
def add_customer():
    data = request.json
    new_customer = create_customer(data)
    return jsonify(new_customer), 201

@customers_bp.route('/<int:customer_id>', methods=['PUT'])
def modify_customer(customer_id):
    data = request.json
    updated_customer = update_customer(customer_id, data)
    if updated_customer:
        return jsonify(updated_customer), 200
    return jsonify({"error": "Customer not found"}), 404

@customers_bp.route('/<int:customer_id>', methods=['DELETE'])
def remove_customer(customer_id):
    if delete_customer(customer_id):
        return jsonify({"message": "Customer deleted"}), 200
    return jsonify({"error": "Customer not found"}), 404
