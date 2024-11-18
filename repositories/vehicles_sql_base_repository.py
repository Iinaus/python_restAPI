import models
from werkzeug.exceptions import NotFound

from services.vehicle_services import VehicleService

class VehiclesSqlBaseRepository:
    def __init__(self, con):
        self.con = con
        
    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute('SELECT * FROM vehicles')
            result = cur.fetchall()
            vehicles = []
            for vehicle in result:
                vehicles.append(models.Vehicle(vehicle[0], vehicle[1], vehicle[2]))
            return vehicles
        
    def get_by_id(self, id):
        with self.con.cursor() as cur:
            cur.execute("SELECT * FROM vehicles WHERE id = %s", (id,))
            vehicle_tuple = cur.fetchone()
            if vehicle_tuple is None:
                raise NotFound('vehicle not found')
            vehicle = VehicleService.vehicle_tuple_to_vehicle(vehicle_tuple)
            return vehicle

    def update_by_id(self, vehicle, req_data):
        try:
            vehicle.make = req_data['make']
            vehicle.model = req_data['model']
            
            with self.con.cursor() as cur:
                sql = """
                        UPDATE vehicles 
                        SET make = %s, model = %s
                        WHERE id = %s
                        """
                values = (vehicle.make, vehicle.model, vehicle.id)
                cur.execute(sql, values)
                self.con.commit()
                vehicle = models.Vehicle(vehicle.id, vehicle.make, vehicle.model)
                return vehicle
        except Exception as e:
            self.con.rollback()
            raise e

    def delete_by_id(self, vehicle):
        try:
            with self.con.cursor() as cur:
                cur.execute("DELETE FROM vehicles WHERE id = %s", (vehicle.id,))
                self.con.commit()
        except Exception as e:
            self.con.rollback()
            raise e