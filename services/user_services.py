import models


class UserService:

    @staticmethod
    def user_tuple_to_user(user_tuple):
        return models.User(
            _id = user_tuple[0],
            username = user_tuple[1],
            firstname = user_tuple[2],
            lastname = user_tuple[3]
        )
    
    @staticmethod
    def list_to_json(users_list):
        json_list = []
        for u in users_list:
            json_list.append(UserService.to_json(u))
        return json_list
    
    @staticmethod
    def to_json(user):
        return {"id": user.id, "username": user.username, "firstname": user.firstname, "lastname": user.lastname}