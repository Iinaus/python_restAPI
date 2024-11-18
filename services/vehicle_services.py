import models


class VehicleService:
    @staticmethod
    def vehicle_tuple_to_vehicle(vehicle_tuple):
        if not isinstance(vehicle_tuple, tuple) or len(vehicle_tuple) != 3:
            raise ValueError("vehicle_tuple must be a tuple of length 3.")

        return models.Vehicle(
            _id = vehicle_tuple[0],
            make = vehicle_tuple[1],
            model = vehicle_tuple[2]
        )
    
    @staticmethod
    def list_to_json(vehicle_list):
        if not isinstance(vehicle_list, list):
            raise ValueError("vehicle_list must be a list.")
        
        json_list = []
        for v in vehicle_list:
            json_list.append(VehicleService.to_json(v))
        return json_list
    
    @staticmethod
    def to_json(vehicle):
        if not isinstance(vehicle, models.Vehicle):
            raise ValueError("Input must be a Vehicle instance.")
        
        return {"id": vehicle.id, "make": vehicle.make, "model": vehicle.model}