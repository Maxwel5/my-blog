from flask import render_template
from . import main
# from flask_login import login_required

# Views
@main.route('/')
def index():

    message = 'Fine Blog'
    return render_template('index.html',message = message)