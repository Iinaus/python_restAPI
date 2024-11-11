import models


class ProductService:
    @staticmethod
    def product_tuple_to_product(product_tuple):
        if not isinstance(product_tuple, tuple) or len(product_tuple) != 3:
            raise ValueError("product_tuple must be a tuple of length 3.")
        
        return models.Product(
            _id = product_tuple[0],
            name = product_tuple[1],
            description = product_tuple[2]
        )
    
    @staticmethod
    def list_to_json(product_list):
        if not isinstance(product_list, list):
            raise ValueError("product_list must be a list.")
        
        json_list = []
        for p in product_list:
            json_list.append(ProductService.to_json(p))
        return json_list
    
    @staticmethod
    def to_json(product):
        if not isinstance(product, models.Product):
            raise ValueError("Input must be a Product instance.")
        
        return {"id": product.id, "name": product.name, "description": product.description}