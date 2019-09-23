from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    message = 'Fine Blog'
    return render_template('index.html')