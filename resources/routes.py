from .api_auth import Login
from resources.api_users import UserApi, UsersApi
from .api_example import Example


def initialize_routes(api):
    api.add_resource(Login, "/login")
    
    api.add_resource(UsersApi, "/users")
    api.add_resource(UserApi, "/users/<public_user_id>")

    api.add_resource(Example, "/api/example)")
