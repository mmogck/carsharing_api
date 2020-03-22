from app import app, db
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

import uuid
from werkzeug.security import generate_password_hash, check_password_hash

from database.models import User
from resources.api_auth import token_required, admin_required
from resources.errors import *

class UsersApi(Resource):
    def get(self):
        users = User.query.all()

        output = []

        for user in users:
            user_data = {}
            user_data['public_user_id'] = user.public_user_id
            user_data['username'] = user.username
            user_data['password'] = user.password
            user_data['admin'] = user.admin
            output.append(user_data)

        return {'users' : output}, 200

    def post(self):
        try:
            data = request.get_json()
            
            if not data["username"] or not data["password"]:
                raise BadRequestError

            hashed_password = generate_password_hash(data["password"], method="sha256")

            new_user = User(public_user_id=str(uuid.uuid4()), username=data["username"], password=hashed_password, admin = data["admin"])

            db.session.add(new_user)
            db.session.commit()

            return {"message" : "New user created!"}, 201
        except Exception:
            raise InternalServerError
    
    def put(self):
        return None

    @admin_required
    def delete(self):
        users = User.query.all()

        for user in users:
            db.session.delete(user)

        db.session.commit()

        return {'message' : 'All users has been deleted!'}, 204

class UserApi(Resource):
    def get(self, public_user_id):
        user = User.query.filter_by(public_user_id=public_user_id).first()

        if not user:
            raise NotFoundError

        user_data = {}
        user_data['public_user_id'] = user.public_user_id
        user_data['username'] = user.username
        user_data['password'] = user.password
        user_data['admin'] = user.admin

        return {'user' : user_data}, 200
    
    def put(self):
        return None

    def delete(self, public_user_id):
        user = User.query.filter_by(public_user_id=public_user_id).first()

        if not user:
            raise NotFoundError

        db.session.delete(user)
        db.session.commit()

        return {'message' : 'The user has been deleted!'}, 204