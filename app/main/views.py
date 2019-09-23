from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    message = 'Fine Blog'
    return render_template('index.html',message = message)