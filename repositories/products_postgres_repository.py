import models

from repositories.products_sql_base_repository import ProductsSqlBaseRepository

class ProductsPostgresRepository(ProductsSqlBaseRepository):
    def __init__(self, con):
        super(ProductsPostgresRepository, self).__init__(con)

    def create(self, product):
        try:
            with self.con.cursor() as cur:
                sql = """
                        INSERT INTO products (name, description)
                        VALUES (%s, %s)
                        RETURNING id
                    """
                values = (product.name, product.description)
                cur.execute(sql, values)
                product_id = cur.fetchone()[0]
                self.con.commit()
                product = models.Product(product_id, product.name, product.description)
                return product
        except Exception as e:
            self.con.rollback()
            raise e