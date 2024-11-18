import models
from repositories.users_sql_base_repository import UsersSqlBaseRepository

class UsersPostgresRepository(UsersSqlBaseRepository):
    def __init__(self, con):
        super(UsersPostgresRepository, self).__init__(con)

    def create(self, user):
        try:
            with self.con.cursor() as cur:
                sql = """
                        INSERT INTO users (username, firstname, lastname)
                        VALUES (%s, %s, %s)
                        RETURNING id
                    """
                values = (user.username, user.firstname, user.lastname)
                cur.execute(sql, values)
                user_id = cur.fetchone()[0]
                self.con.commit()
                user = models.User(user_id, user.username, user.firstname, user.lastname)
                return user
        except Exception as e:
            self.con.rollback()
            raise e