class User:
    def __init__(self, _id, username, firstname, lastname):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

class Product:
    def __init__(self, _id, name, description):
        self.id = _id
        self.name = name
        self.description = description

class Vehicle:
    def __init__(self, _id, make, model):
        self.id = _id
        self.make= make
        self.model = model