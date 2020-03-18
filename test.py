from flask import Flask, request
from flask import jsonify
from datetime import datetime
import re as regex

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = regex.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")