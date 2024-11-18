import models
from werkzeug.exceptions import NotFound

from services.user_services import UserService

class UsersSqlBaseRepository:
    def __init__(self, con):
        self.con = con
        
    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute('SELECT * FROM users')
            result = cur.fetchall()
            users = []
            for user in result:
                users.append(models.User(user[0], user[1], user[2], user[3]))
            return users
        
    def get_by_id(self, id):
        with self.con.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (id,))
            user_tuple = cur.fetchone()
            if user_tuple is None:
                raise NotFound('user not found')
            user = UserService.user_tuple_to_user(user_tuple)
            return user

    def update_by_id(self, user, req_data):
        try:
            user.username = req_data['username']
            user.firstname = req_data['firstname']
            user.lastname = req_data['lastname']
            
            with self.con.cursor() as cur:
                sql = """
                        UPDATE users 
                        SET username = %s, firstname = %s, lastname = %s 
                        WHERE id = %s
                        """
                values = (user.username, user.firstname, user.lastname, user.id)
                cur.execute(sql, values)
                self.con.commit()
                user = models.User(user.id, user.username, user.firstname, user.lastname)
                return user
        except Exception as e:
            self.con.rollback()
            raise e

    def delete_by_id(self, user):
        try:
            with self.con.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id = %s", (user.id,))
                self.con.commit()
        except Exception as e:
            self.con.rollback()
            raise e