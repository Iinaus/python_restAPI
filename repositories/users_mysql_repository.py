import models

from repositories.users_sql_base_repository import UsersSqlBaseRepository

class UsersMysqlRepository(UsersSqlBaseRepository):
    def __init__(self, con):
        super(UsersMysqlRepository, self).__init__(con)

    def create(self, user):
        try:
            with self.con.cursor() as cur:
                sql = """
                        INSERT INTO users (username, firstname, lastname)
                        VALUES (%s, %s, %s)
                        """
                values = (user.username, user.firstname, user.lastname)
                cur.execute(sql, values)
                self.con.commit()
                user.id = cur.lastrowid
                user = models.User(user.id, user.username, user.firstname, user.lastname)
                return user
        except Exception as e:
            self.con.rollback()
            raise e