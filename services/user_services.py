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
            json_list.append(u.to_json())
        return json_list