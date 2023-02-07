#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def info():
    """Displays 'HBNB'"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_info(text):
    """Displays 'C' and other text"""
    text = text.replace('_', ' ')
    return ('C {}'.format(text))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_info(text="is cool"):
    """Displays 'python' with some text"""
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays an integer"""
    return('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an html page if <n> is an integer"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Displays an html page if <n> is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
