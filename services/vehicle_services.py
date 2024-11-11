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
    def list_to_json(users_list):
        json_list = []
        for u in users_list:
            json_list.append(u.to_json())
        return json_list