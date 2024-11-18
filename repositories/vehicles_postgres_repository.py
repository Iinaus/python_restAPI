import models

from repositories.vehicles_sql_base_repository import VehiclesSqlBaseRepository

class VehiclesPostgresRepository(VehiclesSqlBaseRepository):
    def __init__(self, con):
        super(VehiclesPostgresRepository, self).__init__(con)

    def create(self, vehicle):
        try:
            with self.con.cursor() as cur:
                sql = """
                        INSERT INTO vehicles (make, model)
                        VALUES (%s, %s)
                        RETURNING id
                    """
                values = (vehicle.make, vehicle.model)
                cur.execute(sql, values)
                vehicle_id = cur.fetchone()[0]
                self.con.commit()
                vehicle = models.Vehicle(vehicle_id, vehicle.make, vehicle.model)
                return vehicle
        except Exception as e:
            self.con.rollback()
            raise e