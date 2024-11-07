from flask import jsonify

from decorators.db_connection_decorator import get_db_connection
from decorators.repository_decorator import get_repository

@get_db_connection
@get_repository('vehicles')
def get_all_vehicles(repo):
    try:
        repo.get_all()
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('vehicles')
def get_vehicle_by_id(repo, id):
    try:
        repo.get_by_id()
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('vehicles')
def create_vehicle(repo):
    try:
        repo.create()
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('vehicles')
def update_vehicle_by_id(repo, id):
    try:
        repo.update_by_id()
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('vehicles')
def delete_vehicle_by_id(repo, id):
    try:
        repo.delete_by_id()
    except Exception as e:
        return jsonify({'err': str(e)}), 500