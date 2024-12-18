from repositories.repository_factory import products_repository_factory, users_repository_factory, vehicles_repository_factory
from services.user_services import UserService
from services.product_services import ProductService
from services.vehicle_services import VehicleService


def get_repository_and_service(name):
    def decorator(route_handler):
        def wrapper(con, *args, **kwargs):
            repo = None
            try:
                if name == 'users':
                    repo = users_repository_factory(con)
                    service = UserService
                elif name == 'products':
                    repo = products_repository_factory(con)
                    service = ProductService
                elif name == 'vehicles':
                    repo = vehicles_repository_factory(con)
                    service = VehicleService
                else:
                    raise ValueError(f"Unknown repository name '{name}'")

            except Exception as e:
                raise ValueError(f"Failed to initialize repository: {e}.")
            
            return route_handler(repo, service, *args, **kwargs)
        return wrapper
    return decorator