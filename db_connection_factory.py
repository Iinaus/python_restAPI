import contextlib
import mysql.connector
import psycopg2
import pymongo
from config import Config

@contextlib.contextmanager
def con_factory():
    con = None
    client = None 
    try:
        _db = Config.DB
        _db_name = Config.DATABASE_NAME
        _db_password = Config.DATABASE_PASSWORD

        if _db == 'mysql':
            con = mysql.connector.connect(user='root', database=_db_name)
        elif _db == 'postgres':
            con = psycopg2.connect(database=_db_name, user='postgres', password=_db_password)
        elif _db == 'mongoDB':
            client = pymongo.MongoClient('mongodb://localhost:27017/')
            con = client[_db_name]
        
        yield con

    finally:
        if con is not None:
            if _db in ['mysql', 'postgres']:
                con.close()

        if client is not None:
            client.close()