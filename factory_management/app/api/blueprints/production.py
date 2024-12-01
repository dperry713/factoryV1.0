from flask import Blueprint, request, jsonify
from app.services.production_service import (
    get_all_production_records,
    get_production_record_by_id,
    create_production_record,
    update_production_record,
    delete_production_record,
)

production_bp = Blueprint('production', __name__)

@production_bp.route('/', methods=['GET'])
def list_production_records():
    production_records = get_all_production_records()
    return jsonify(production_records), 200

@production_bp.route('/<int:production_id>', methods=['GET'])
def get_production_record(production_id):
    production_record = get_production_record_by_id(production_id)
    if production_record:
        return jsonify(production_record), 200
    return jsonify({"error": "Production record not found"}), 404

@production_bp.route('/', methods=['POST'])
def add_production_record():
    data = request.json
    new_production_record = create_production_record(data)
    return jsonify(new_production_record), 201

@production_bp.route('/<int:production_id>', methods=['PUT'])
def modify_production_record(production_id):
    data = request.json
    updated_production_record = update_production_record(production_id, data)
    if updated_production_record:
        return jsonify(updated_production_record), 200
    return jsonify({"error": "Production record not found"}), 404

@production_bp.route('/<int:production_id>', methods=['DELETE'])
def remove_production_record(production_id):
    if delete_production_record(production_id):
        return jsonify({"message": "Production record deleted"}), 200
    return jsonify({"error": "Production record not found"}), 404
