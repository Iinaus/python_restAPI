from bson import ObjectId
import models
from werkzeug.exceptions import NotFound

class VehiclesMongodbRepository:
    def __init__(self, con):
        self.con = con
        self.vehicles_collection = self.con['vehicles']
        
    def get_all(self):
        result = self.vehicles_collection.find()
        vehicles = []
        for vehicle in result:
            vehicles.append(models.Vehicle(str(vehicle['_id']), vehicle['make'], vehicle['model']))
        return vehicles
        
    def get_by_id(self, id):
        result = self.vehicles_collection.find_one({"_id": ObjectId(id)})
        if result is None:
            raise NotFound('vehicle not found')
        vehicle = models.Vehicle(str(result['_id']), result['make'], result['model'])
        return vehicle

    def create(self, vehicle):
        try:
            result = self.vehicles_collection.insert_one({"make": vehicle.make, "model": vehicle.model})
            vehicle = models.Vehicle(str(result.inserted_id), vehicle.make, vehicle.model)
            return vehicle
        except Exception as e:
            raise e

    def update_by_id(self, vehicle, req_data):
        try:
            vehicle.make = req_data['make']
            vehicle.model = req_data['model']
            
            self.vehicles_collection.update_one(
                {"_id": ObjectId(vehicle.id)},
                {"$set": {"make": vehicle.make, "model": vehicle.model}}
            )

            vehicle = models.Vehicle(vehicle.id, vehicle.make, vehicle.model)
            return vehicle
        except Exception as e:
            raise e

    def delete_by_id(self, vehicle):
        try:
            self.vehicles_collection.delete_one({"_id": ObjectId(vehicle.id)})
        except Exception as e:
            raise e