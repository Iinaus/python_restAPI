import models


class ProductService:
    @staticmethod
    def product_tuple_to_product(product_tuple):
        return models.Product(
            _id = product_tuple[0],
            name = product_tuple[1],
            description = product_tuple[2]
        )
    
    @staticmethod
    def list_to_json(product_list):
        json_list = []
        for p in product_list:
            json_list.append(ProductService.to_json(p))
        return json_list
    
    @staticmethod
    def to_json(product):
        return {"id": product.id, "name": product.name, "description": product.description}