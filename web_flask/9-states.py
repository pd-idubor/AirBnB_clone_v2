#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """States by cities, with id"""
    state_obj = storage.all(State)

    for value in state_obj.values():
        if (value.id == id):
            return render_template('9-states.html', state=value)

    states = []
    for value in state_obj.values():
        states.append(value)
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Closes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
