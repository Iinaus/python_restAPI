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
    def list_to_json(users_list):
        json_list = []
        for u in users_list:
            json_list.append(u.to_json())
        return json_list