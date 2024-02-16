#!/usr/bin/python3
"""
start a flask web application
"""
from flask import Flask
web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def say_hello():
    """ Function that says Hello """
    return 'Hello HBNB!'


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
