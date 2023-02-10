#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays cities by states"""
    state_obj = storage.all(State)
    states = []

    for value in state_obj.values():
        states.append(value)

    return render_template('8-cities_by_states.html',
                           states=states)


@app.teardown_appcontext
def teardown(exception):
    """Closes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
