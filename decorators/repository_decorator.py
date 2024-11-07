from repositories.repository_factory import products_repository_factory, users_repository_factory, vehicles_repository_factory


def get_repository(name):
    def decorator(route_handler):
        def wrapper(*args, **kwargs):
            repo = None
            try:
                if name == 'users':
                    repo = users_repository_factory()
                elif name == 'products':
                    repo = products_repository_factory()
                elif name == 'vehicles':
                    repo = vehicles_repository_factory()
                else:
                    raise ValueError(f"Unknown repository name '{name}'")

            except Exception as e:
                raise ValueError(f"Failed to initialize repository: {e}.")
            
            return route_handler(repo, *args, **kwargs)
        return wrapper
    return decorator