#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def dispose(exception):
    """ Remove current ssqlalchemy ession """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states():
    """ Display list of states in db"""
    states = storage.all(State)
    states_list = list(states.values())
    return render_template('8-cities_by_states.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)