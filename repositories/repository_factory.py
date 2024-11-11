from config import Config
from repositories.products_mongodb_repository import ProductsMongodbRepository
from repositories.products_mysql_repository import ProductsMysqlRepository
from repositories.products_postgres_repository import ProductsPostgresRepository
from repositories.users_mongodb_repository import UsersMongodbRepository
from repositories.users_mysql_repository import UsersMysqlRepository
from repositories.users_postgres_repository import UsersPostgresRepository
from repositories.vehicles_mongodb_repository import VehiclesMongodbRepository
from repositories.vehicles_mysql_repository import VehiclesMysqlRepository
from repositories.vehicles_postgres_repository import VehiclesPostgresRepository


def users_repository_factory(con):
    _db = Config.DB
    if _db == 'mysql':
        return UsersMysqlRepository(con)
    elif _db == 'postgres':
        return UsersPostgresRepository(con)
    elif _db == 'mongoDB':
        return UsersMongodbRepository(con)
    else:
        raise ValueError(f"Invalid database type: {_db}. Accepted values are: mysql, postgres, mongoDB.")

def products_repository_factory(con):
    _db = Config.DB
    if _db == 'mysql':
        return ProductsMysqlRepository(con)
    elif _db == 'postgres':
        return ProductsPostgresRepository(con)
    elif _db == 'mongoDB':
        return ProductsMongodbRepository(con)
    else:
        raise ValueError(f"Invalid database type: {_db}. Accepted values are: mysql, postgres, mongoDB.")
    
def vehicles_repository_factory(con):
    _db = Config.DB
    if _db == 'mysql':
        return VehiclesMysqlRepository(con)
    elif _db == 'postgres':
        return VehiclesPostgresRepository(con)
    elif _db == 'mongoDB':
        return VehiclesMongodbRepository(con)
    else:
        raise ValueError(f"Invalid database type: {_db}. Accepted values are: mysql, postgres, mongoDB.")