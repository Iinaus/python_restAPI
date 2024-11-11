from flask import jsonify, request
from werkzeug.exceptions import NotFound

from decorators.db_connection_decorator import get_db_connection
from decorators.repository_decorator import get_repository_and_service
import models

@get_db_connection
@get_repository_and_service('vehicles')
def get_all_vehicles(repo, service):
    try:
        vehicles = repo.get_all()
        vehicles_json = service.list_to_json(vehicles)
        return jsonify(vehicles_json)
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository_and_service('vehicles')
def get_vehicle_by_id(repo, service, id):
    try:
        vehicle = repo.get_by_id(id)
        return jsonify(service.to_json(vehicle))
    except NotFound:
        return jsonify({'err': 'vehicle not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository_and_service('vehicles')
def create_vehicle(repo, service):
    try:
        req_data = request.get_json()
        new_vehicle = models.Vehicle(0, req_data['make'], req_data['model'])
        vehicle = repo.create(new_vehicle)
        return jsonify(service.to_json(vehicle))
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository_and_service('vehicles')
def update_vehicle_by_id(repo, service, id):
    try:
        vehicle = repo.get_by_id(id)
        req_data = request.get_json()
        updated_vehicle = repo.update_by_id(vehicle, req_data)
        return jsonify(service.to_json(updated_vehicle))
    except NotFound:
        return jsonify({'err': 'vehicle not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository_and_service('vehicles')
def delete_vehicle_by_id(repo, service, id):
    try:
        vehicle = repo.get_by_id(id)
        repo.delete_by_id(vehicle)
        return jsonify(), 200
    except NotFound:
        return jsonify({'err': 'vehicle not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500