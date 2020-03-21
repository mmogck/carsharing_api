from app import app, db
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from database.models import Example

from resources.api_auth import token_required
from resources.errors import InternalServerError


class Example(Resource):
    def get(self):
        try:
            return ""
        except Exception:
            raise InternalServerError
    
    def post(self):
        try:
            return ""
        except Exception:
            raise InternalServerError
    
    def put(self):
        try:
            return ""
        except Exception:
            raise InternalServerError
    
    def delete(self):
        try:
            return ""
        except Exception:
            raise InternalServerError

