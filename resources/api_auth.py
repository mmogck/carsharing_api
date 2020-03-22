from app import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

import jwt
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

from database.models import User
from resources.errors import *


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            raise BadRequestError

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            from database.models import User
            current_user = User.query.filter_by(public_user_id=data['public_user_id']).first()
        except:
            raise UnauthorizedError

        return f(current_user, *args, **kwargs)

    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            raise BadRequestError

        data = jwt.decode(token, app.config['SECRET_KEY'])
        user = User.query.filter_by(public_user_id=data["public_user_id"]).first()

        if not user.admin:
            raise UnauthorizedError

        return f(*args, **kwargs)

    return decorated

class Login(Resource):
    def get(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            raise BadRequestError

        from database.models import User
        user = User.query.filter_by(username=auth.username).first()

        if not user:
            raise NotFoundError

        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_user_id' : user.public_user_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

            return {'token' : token.decode('UTF-8')}, 200

        raise UnauthorizedError