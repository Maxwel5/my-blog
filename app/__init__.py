from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootsrap = Bootstrap()

# Creating the app configurations
app.config.from_object(config_options[config_name])

def create_app(config_name):
    app = Flask(__name__)

#initialising blueprints
bootstrap.init_app(app)

# Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from app import views

return app

