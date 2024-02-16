#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def say_hello():
    """ Function that sys Hello"""
    return 'Hello HBNB!'


@web_app.route('/hbnb')
def hbnb():
    """ Function that says hbnb """
    return 'HBNB'


@web_app.route('/c/<text>')
def c_text(text):
    """ Display C + message """
    message = text.replace('_', ' ')
    #return f" C {message}"
    return 'C %s' % message


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
