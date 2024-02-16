#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
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
    '''return f" C {message}'''
    return 'C %s' % message


@web_app.route('/python/')
@web_app.route('/python/<text>')
def python_text(text='is_cool'):
    """ Display Python message """
    message = text.replace('_', ' ')
    return 'Python %s' % message


@web_app.route('/number/<int:n>')
def display_number(n):
    """ Display n is a number only if n is an integer """
    return "%d is a number" % n


@web_app.route('/number_template/<int:n>')
def html_page(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
