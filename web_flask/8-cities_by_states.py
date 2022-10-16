#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models import State

app = Flask("__name__")


@app.teardown_appcontext
def refresh(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def route_states():
    data = storage.all(State)
    states = data.values()
    return render_template('7-states_list.html', states_list=states)


@app.route("/cities_by_states", strict_slashes=False)
def route_city():
    data = storage.all(State)
    states = data.values()
    return render_template('8-cities_by_states.html', states_list=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
