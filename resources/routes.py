from .api_example import Example


def initialize_routes(api):
    api.add_resource(Example, "/api/example)")
