from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import os

from resources.errors import errors


APP_DEBUG                       = True
APP_HOST                        = "localhost"
APP_PORT                        = "5002"
APP_SSL                         = None
APP_SECRET_KEY                  = "secretkey"
APP_ERRORS                      = errors
APP_DB_URI                      = "sqlite3:///"  + os.path.abspath("database/db.sqlite3")
APP_DB_TRACK_MODIFICATIONS      = True

app = Flask(__name__)

app.config["SECRET_KEY"]                        = APP_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"]           = APP_DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]    = APP_DB_TRACK_MODIFICATIONS

api = Api(app, errors=APP_ERRORS)
db = SQLAlchemy(app)

import database.models

if __name__ == '__main__':
    from resources.routes import initialize_routes
    initialize_routes(api)
    app.run(debug=APP_DEBUG, host=APP_HOST, port=APP_PORT, ssl_context=APP_SSL)