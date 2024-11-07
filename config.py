import os

class Config:
    DB = os.getenv('DB')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')