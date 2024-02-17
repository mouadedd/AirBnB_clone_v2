#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def dispose(exception):
    """ Remove current sqlalchemy session """
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>')
def states_and_state(id=None):
    """ Display list of states in db"""
    if id:
        id = 'State.{}'.format(id)
    return render_template('9-states.html', states=storage.all(State), id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
