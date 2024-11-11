import models


class VehicleService:
    @staticmethod
    def vehicle_tuple_to_vehicle(vehicle_tuple):
        return models.Vehicle(
            _id = vehicle_tuple[0],
            make = vehicle_tuple[1],
            model = vehicle_tuple[2]
        )
    
    @staticmethod
    def list_to_json(vehicle_list):
        json_list = []
        for v in vehicle_list:
            json_list.append(VehicleService.to_json(v))
        return json_list
    
    @staticmethod
    def to_json(vehicle):
        return {"id": vehicle.id, "make": vehicle.make, "model": vehicle.model}