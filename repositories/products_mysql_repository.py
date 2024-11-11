import models
from werkzeug.exceptions import NotFound

from services.product_services import ProductService

class ProductsMysqlRepository:
    def __init__(self, con):
        self.con = con
        
    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute('SELECT * FROM products')
            result = cur.fetchall()
            products = []
            for product in result:
                products.append(models.Product(product[0], product[1], product[2]))
            return products
        
    def get_by_id(self, id):
        with self.con.cursor() as cur:
            cur.execute("SELECT * FROM products WHERE id = %s", (id,))
            product_tuple = cur.fetchone()
            if product_tuple is None:
                raise NotFound('product not found')
            product = ProductService.product_tuple_to_product(product_tuple)
            return product

    def create(self, product):
        try:
            with self.con.cursor() as cur:
                sql = """
                        INSERT INTO products (name, description)
                        VALUES (%s, %s)
                        """
                values = (product.name, product.description)
                cur.execute(sql, values)
                self.con.commit()
                product.id = cur.lastrowid
                product = models.Product(product.id, product.name, product.description)
                return product
        except Exception as e:
            self.con.rollback()
            raise e

    def update_by_id(self, product, req_data):
        try:
            product.name = req_data['name']
            product.description = req_data['description']
            
            with self.con.cursor() as cur:
                sql = """
                        UPDATE products 
                        SET name = %s, description = %s
                        WHERE id = %s
                        """
                values = (product.name, product.description, product.id)
                cur.execute(sql, values)
                self.con.commit()
                product = models.Product(product.id, product.name, product.description)
                return product
        except Exception as e:
            self.con.rollback()
            raise e

    def delete_by_id(self, product):
        try:
            with self.con.cursor() as cur:
                cur.execute("DELETE FROM products WHERE id = %s", (product.id,))
                self.con.commit()
        except Exception as e:
            self.con.rollback()
            raise e