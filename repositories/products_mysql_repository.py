import models

from repositories.products_sql_base_repository import ProductsSqlBaseRepository

class ProductsMysqlRepository(ProductsSqlBaseRepository):
    def __init__(self, con):
        super(ProductsMysqlRepository, self).__init__(con)
    
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