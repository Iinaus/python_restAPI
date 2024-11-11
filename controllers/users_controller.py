from flask import jsonify, request
from werkzeug.exceptions import NotFound

from decorators.db_connection_decorator import get_db_connection
from decorators.repository_decorator import get_repository
import models
import services.user_services

@get_db_connection
@get_repository('users')
def get_all_users(repo):
    try:
        users = repo.get_all()
        users_json = services.user_services.UserService.list_to_json(users)
        return jsonify(users_json)
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('users')
def get_user_by_id(repo, id):
    try:
        user = repo.get_by_id(id)
        return jsonify(user.to_json())
    except NotFound:
        return jsonify({'err': 'user not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('users')
def create_user(repo):
    try:
        req_data = request.get_json()
        new_user = models.User(0, req_data['username'], req_data['firstname'], req_data['lastname'])
        user = repo.create(new_user)
        return jsonify(user.to_json())
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('users')
def update_user_by_id(repo, id):
    try:
        user = repo.get_by_id(id)
        req_data = request.get_json()
        updated_user = repo.update_by_id(user, req_data)
        return jsonify(updated_user.to_json())
    except NotFound:
        return jsonify({'err': 'user not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('users')
def delete_user_by_id(repo, id):
    try:
        user = repo.get_by_id(id)
        repo.delete_by_id(user)
        return jsonify(), 200
    except NotFound:
        return jsonify({'err': 'user not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500