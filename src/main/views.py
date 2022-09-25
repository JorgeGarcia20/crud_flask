from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')


'''
Commands to the correct execution app
export FLASK_APP=app.py
export FLASK_DEBUG=1
'''
