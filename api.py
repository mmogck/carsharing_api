from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
from json import dumps
from flask import jsonify


app = Flask(__name__)
api = Api(app)


class Test(Resource):
    def get(self):
        return {'Hello World'}


api.add_resource(Test, '/test')

if __name__ == '__main__':
     app.run(port='5002')