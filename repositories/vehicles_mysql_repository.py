import models

from repositories.vehicles_sql_base_repository import VehiclesSqlBaseRepository

class VehiclesMysqlRepository(VehiclesSqlBaseRepository):
    def __init__(self, con):
        super(VehiclesMysqlRepository, self).__init__(con)

    def create(self, vehicle):
        try:
            with self.con.cursor() as cur:
                sql = """
                        INSERT INTO vehicles (make, model)
                        VALUES (%s, %s)
                        """
                values = (vehicle.make, vehicle.model)
                cur.execute(sql, values)
                self.con.commit()
                vehicle.id = cur.lastrowid
                vehicle = models.Vehicle(vehicle.id, vehicle.make, vehicle.model)
                return vehicle
        except Exception as e:
            self.con.rollback()
            raise e