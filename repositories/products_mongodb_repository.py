from bson import ObjectId
import models
from werkzeug.exceptions import NotFound

class ProductsMongodbRepository:
    def __init__(self, con):
        self.con = con
        self.products_collection = self.con['products']
        
    def get_all(self):
        result = self.products_collection.find()
        products = []
        for product in result:
            products.append(models.Product(str(product['_id']), product['name'], product['description']))
        return products
        
    def get_by_id(self, id):
        result = self.products_collection.find_one({"_id": ObjectId(id)})
        if result is None:
            raise NotFound('product not found')
        product = models.Product(str(result['_id']), result['name'], result['description'])
        return product

    def create(self, product):
        try:
            result = self.products_collection.insert_one({"name": product.name, "description": product.description})
            product = models.Product(str(result.inserted_id), product.name, product.description)
            return product
        except Exception as e:
            raise e

    def update_by_id(self, product, req_data):
        try:
            product.name = req_data['name']
            product.description = req_data['description']
            
            self.products_collection.update_one(
                {"_id": ObjectId(product.id)},
                {"$set": {"name": product.name, "description": product.description}}
            )

            product = models.Product(product.id, product.name, product.description)
            return product
        except Exception as e:
            raise e

    def delete_by_id(self, product):
        try:
            self.products_collection.delete_one({"_id": ObjectId(product.id)})
        except Exception as e:
            raise e