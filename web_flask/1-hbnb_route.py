#!/usr/bin/python3
""" Start a Flask web application """
from flask import Flask
web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def say_hello():
    """ Function that says Hello"""
    return 'Hello HBNB!'


@web_app.route('/hbnb')
def hbnb():
    """ Function that says hbnb """
    return 'HBNB'


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
