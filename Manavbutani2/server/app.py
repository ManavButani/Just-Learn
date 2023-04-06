""" this is main file for running the flask application
"""
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from controllers import *

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")