from bson import ObjectId
import models
from werkzeug.exceptions import NotFound


class UsersMongodbRepository:
    def __init__(self, con):
        self.con = con
        self.users_collection = self.con['users']
    
    def get_all(self):
        result = self.users_collection.find()
        users = []
        for user in result:
            users.append(models.User(str(user['_id']), user['username'], user['firstname'], user['lastname']))
        return users
        
    def get_by_id(self, id):
        result = self.users_collection.find_one({"_id": ObjectId(id)})
        if result is None:
            raise NotFound('user not found')
        user = models.User(str(result['_id']), result['username'], result['firstname'], result['lastname'])
        return user

    def create(self, user):
        try:
            result = self.users_collection.insert_one({"firstname": user.firstname, "lastname": user.lastname, "username": user.username})
            user = models.User(str(result.inserted_id), user.username, user.firstname, user.lastname)
            return user
        except Exception as e:
            raise e

    def update_by_id(self, user, req_data):
        try:
            user.username = req_data['username']
            user.firstname = req_data['firstname']
            user.lastname = req_data['lastname']
            
            self.users_collection.update_one(
                {"_id": ObjectId(user.id)},
                {"$set": {"firstname": user.firstname, "lastname": user.lastname, "username": user.username}}
            )

            user = models.User(user.id, user.username, user.firstname, user.lastname)
            return user
        except Exception as e:
            raise e

    def delete_by_id(self, user):
        try:
            self.users_collection.delete_one({"_id": ObjectId(user.id)})
        except Exception as e:
            raise e