from flask import jsonify

from decorators.db_connection_decorator import get_db_connection
from decorators.repository_decorator import get_repository

@get_db_connection
@get_repository('users')
def get_all_users(repo):
    try:
        repo.get_all()
        print('##### Users_controller / get_all_users: TOIMII')
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('users')
def get_user_by_id(repo, id):
    try:
        repo.get_by_id()
        print('##### Users_controller / get_by_id: TOIMII')
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('users')
def create_user(repo):
    try:
        repo.create()
        print('##### Users_controller / create: TOIMII')
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('users')
def update_user_by_id(repo, id):
    try:
        repo.update_by_id()
        print('##### Users_controller / update_by_id: TOIMII')
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('users')
def delete_user_by_id(repo, id):
    try:
        repo.delete_by_id()
        print('##### Users_controller / delete_by_id: TOIMII')
    except Exception as e:
        return jsonify({'err': str(e)}), 500