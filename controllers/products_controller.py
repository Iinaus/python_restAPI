from flask import jsonify, request
from werkzeug.exceptions import NotFound

from decorators.db_connection_decorator import get_db_connection
from decorators.repository_decorator import get_repository_and_service
import models

@get_db_connection
@get_repository_and_service('products')
def get_all_products(repo, service):
    try:
        products = repo.get_all()
        products_json = service.list_to_json(products)
        return jsonify(products_json)
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository_and_service('products')
def get_product_by_id(repo, service, id):
    try:
        product = repo.get_by_id(id)
        return jsonify(service.to_json(product))
    except NotFound:
        return jsonify({'err': 'product not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository_and_service('products')
def create_product(repo, service):
    try:
        req_data = request.get_json()
        new_product = models.Product(0, req_data['name'], req_data['description'])
        product = repo.create(new_product)
        return jsonify(service.to_json(product))
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository_and_service('products')
def update_product_by_id(repo, service, id):
    try:
        product = repo.get_by_id(id)
        req_data = request.get_json()
        updated_product = repo.update_by_id(product, req_data)
        return jsonify(service.to_json(updated_product))
    except NotFound:
        return jsonify({'err': 'product not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500

@get_db_connection
@get_repository_and_service('products')
def delete_product_by_id(repo, service, id):
    try:
        product = repo.get_by_id(id)
        repo.delete_by_id(product)
        return jsonify(), 200
    except NotFound:
        return jsonify({'err': 'product not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500