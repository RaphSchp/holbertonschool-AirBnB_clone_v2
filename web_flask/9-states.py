#!/usr/bin/python3
''' 
This is a Flask web application for handling states and cities.

It includes routes for displaying a list of states and information about a specific state.

Author: Your Name
'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def state_ls():
    '''Displays a list of all states.'''
    states = storage.all("State").values()
    return render_template('9-states.html', states=states, mode='all')

@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    '''Displays information about a specific state based on the provided ID.'''
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode=';')

@app.teardown_appcontext
def storage_close(self):
    '''Closes the storage connection after each request.'''
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
