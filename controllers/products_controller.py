from flask import jsonify

from decorators.db_connection_decorator import get_db_connection
from decorators.repository_decorator import get_repository

@get_db_connection
@get_repository('products')
def get_all_products(repo):
    try:
        repo.get_all()
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('products')
def get_product_by_id(repo, id):
    try:
        repo.get_by_id()
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('products')
def create_product(repo):
    try:
        repo.create()
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('products')
def update_product_by_id(repo, id):
    try:
        repo.update_by_id()
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository('products')
def delete_product_by_id(repo, id):
    try:
        repo.delete_by_id()
    except Exception as e:
        return jsonify({'err': str(e)}), 500