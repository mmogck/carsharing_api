class InternalServerError(Exception):
    pass

class BadRequestError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class ForbidenError(Exception):
    pass

class NotFoundError(Exception):
    pass

class MethodNotAllowedError(Exception):
    pass

class NotAcceptableError(Exception):
    pass

class RequestTimeoutError(Exception):
    pass

class ConflictError(Exception):
    pass

class GoneError(Exception):
    pass

class RequestEntityTooLargeError(Exception):
    pass

errors = {
    "InternalServerError": {
        "status": 500,
        "message": "Something went wrong"
    },
    "BadRequestError": {
        "status": 400,
        "message": "Something went wrong"
    },
    "UnauthorizedError": {
        "status": 401,
        "message": "Invalid username or password"
    },
    "ForbidenError": {
        "status": 403,
        "message": ""
    },
    "NotFoundError": {
        "status": 404,
        "message": ""
    },
    "MethodNotAllowedError": {
        "status": 405,
        "message": ""
    },
    "NotAcceptableError": {
        "status": 406,
        "message": ""
    },
    "RequestTimeoutError": {
        "status": 408,
        "message": ""
    },
    "ConflictError": {
        "status": 409,
        "message": ""
    },
    "GoneError": {
        "status": 410,
        "message": ""
    },
    "RequestEntityTooLargeError": {
        "status": 413,
        "message": ""
    }
}