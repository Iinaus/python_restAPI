from dotenv import load_dotenv
from flask import Flask

from controllers import products_controller, users_controller, vehicles_controller

app = Flask(__name__)

app.add_url_rule('/api/users', endpoint='get_all_users', view_func=users_controller.get_all_users, methods=['GET'])
app.add_url_rule('/api/users/<id>', endpoint='get_user_by_id', view_func=users_controller.get_user_by_id, methods=['GET'])
app.add_url_rule('/api/users', endpoint='create_user', view_func=users_controller.create_user, methods=['POST'])
app.add_url_rule('/api/users/<id>', endpoint='update_user_by_id', view_func=users_controller.update_user_by_id, methods=['PUT'])
app.add_url_rule('/api/users/<id>', endpoint='delete_user_by_id', view_func=users_controller.delete_user_by_id, methods=['DELETE'])

app.add_url_rule('/api/products', endpoint='get_all_products', view_func=products_controller.get_all_products, methods=['GET'])
app.add_url_rule('/api/products/<id>', endpoint='get_product_by_id', view_func=products_controller.get_product_by_id, methods=['GET'])
app.add_url_rule('/api/products', endpoint='create_product', view_func=products_controller.create_product, methods=['POST'])
app.add_url_rule('/api/products/<id>', endpoint='update_product_by_id', view_func=products_controller.update_product_by_id, methods=['PUT'])
app.add_url_rule('/api/products/<id>', endpoint='delete_product_by_id', view_func=products_controller.delete_product_by_id, methods=['DELETE'])

app.add_url_rule('/api/vehicles', endpoint='get_all_vehicles', view_func=vehicles_controller.get_all_vehicles, methods=['GET'])
app.add_url_rule('/api/vehicles/<id>', endpoint='get_vehicle_by_id', view_func=vehicles_controller.get_vehicle_by_id, methods=['GET'])
app.add_url_rule('/api/vehicles', endpoint='create_vehicle', view_func=vehicles_controller.create_vehicle, methods=['POST'])
app.add_url_rule('/api/vehicles/<id>', endpoint='update_vehicle_by_id', view_func=vehicles_controller.update_vehicle_by_id, methods=['PUT'])
app.add_url_rule('/api/vehicles/<id>', endpoint='delete_vehicle_by_id', view_func=vehicles_controller.delete_vehicle_by_id, methods=['DELETE'])

if __name__ == '__main__':
    load_dotenv()
    app.run()