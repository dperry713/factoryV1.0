from flask import Blueprint, request, jsonify
from app.services.employee_service import (
    get_all_employees,
    get_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
)

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/', methods=['GET'])
def list_employees():
    employees = get_all_employees()
    return jsonify(employees), 200

@employees_bp.route('/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        return jsonify(employee), 200
    return jsonify({"error": "Employee not found"}), 404

@employees_bp.route('/', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = create_employee(data)
    return jsonify(new_employee), 201

@employees_bp.route('/<int:employee_id>', methods=['PUT'])
def modify_employee(employee_id):
    data = request.json
    updated_employee = update_employee(employee_id, data)
    if updated_employee:
        return jsonify(updated_employee), 200
    return jsonify({"error": "Employee not found"}), 404

@employees_bp.route('/<int:employee_id>', methods=['DELETE'])
def remove_employee(employee_id):
    if delete_employee(employee_id):
        return jsonify({"message": "Employee deleted"}), 200
    return jsonify({"error": "Employee not found"}), 404
