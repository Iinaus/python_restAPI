class User:
    def __init__(self, _id, username, firstname, lastname):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    def to_json(self):
        return {"id": self.id, "username": self.username, "firstname": self.firstname, "lastname": self.lastname}

class Product:
    def __init__(self, _id, name, description):
        self.id = _id
        self.name = name
        self.description = description

    def to_json(self):
        return {"id": self.id, "name": self.name, "description": self.description}

class Vehicle:
    def __init__(self, _id, make, model):
        self.id = _id
        self.make= make
        self.model = model

    def to_json(self):
        return {"id": self.id, "make": self.make, "model": self.model}