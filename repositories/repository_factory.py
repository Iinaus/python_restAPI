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


def users_repository_factory():
    _db = Config.DB
    print(_db)
    if _db == 'mysql':
        return UsersMysqlRepository()
    elif _db == 'postgres':
        return UsersPostgresRepository()
    elif _db == 'mongoDB':
        return UsersMongodbRepository()
    else:
        raise ValueError(f"Invalid database type: {_db}. Accepted values are: mysql, postgres, mongoDB.")

def products_repository_factory():
    _db = Config.DB
    if _db == 'mysql':
        return ProductsMysqlRepository()
    elif _db == 'postgres':
        return ProductsPostgresRepository()
    elif _db == 'mongoDB':
        return ProductsMongodbRepository()
    else:
        raise ValueError(f"Invalid database type: {_db}. Accepted values are: mysql, postgres, mongoDB.")
    
def vehicles_repository_factory():
    _db = Config.DB
    if _db == 'mysql':
        return VehiclesMysqlRepository()
    elif _db == 'postgres':
        return VehiclesPostgresRepository()
    elif _db == 'mongoDB':
        return VehiclesMongodbRepository()
    else:
        raise ValueError(f"Invalid database type: {_db}. Accepted values are: mysql, postgres, mongoDB.")