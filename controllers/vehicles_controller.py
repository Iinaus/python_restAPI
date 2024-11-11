from flask import jsonify, request
from werkzeug.exceptions import NotFound

from decorators.db_connection_decorator import get_db_connection
from decorators.repository_decorator import get_repository
import models
import services.vehicle_services

@get_db_connection
@get_repository('vehicles')
def get_all_vehicles(repo):
    try:
        vehicles = repo.get_all()
        vehicles_json = services.vehicle_services.VehicleService.list_to_json(vehicles)
        return jsonify(vehicles_json)
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('vehicles')
def get_vehicle_by_id(repo, id):
    try:
        vehicle = repo.get_by_id(id)
        return jsonify(vehicle.to_json())
    except NotFound:
        return jsonify({'err': 'vehicle not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('vehicles')
def create_vehicle(repo):
    try:
        req_data = request.get_json()
        new_vehicle = models.Vehicle(0, req_data['make'], req_data['model'])
        vehicle = repo.create(new_vehicle)
        return jsonify(vehicle.to_json())
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('vehicles')
def update_vehicle_by_id(repo, id):
    try:
        vehicle = repo.get_by_id(id)
        req_data = request.get_json()
        updated_vehicle = repo.update_by_id(vehicle, req_data)
        return jsonify(updated_vehicle.to_json())
    except NotFound:
        return jsonify({'err': 'vehicle not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('vehicles')
def delete_vehicle_by_id(repo, id):
    try:
        vehicle = repo.get_by_id(id)
        repo.delete_by_id(vehicle)
        return jsonify(), 200
    except NotFound:
        return jsonify({'err': 'vehicle not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500