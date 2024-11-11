import models


class UserService:

    @staticmethod
    def user_tuple_to_user(user_tuple):
        if not isinstance(user_tuple, tuple) or len(user_tuple) != 4:
            raise ValueError("user_tuple must be a tuple of length 4.")
        
        return models.User(
            _id = user_tuple[0],
            username = user_tuple[1],
            firstname = user_tuple[2],
            lastname = user_tuple[3]
        )
    
    @staticmethod
    def list_to_json(users_list):
        if not isinstance(users_list, list):
            raise ValueError("users_list must be a list.")
        
        json_list = []
        for u in users_list:
            json_list.append(UserService.to_json(u))
        return json_list
    
    @staticmethod
    def to_json(user):
        if not isinstance(user, models.User):
            raise ValueError("Input must be a User instance.")
        
        return {"id": user.id, "username": user.username, "firstname": user.firstname, "lastname": user.lastname}