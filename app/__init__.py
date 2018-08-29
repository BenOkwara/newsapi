from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__, instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views



# We pass in instance_relative_config
# which allow us to connect to the instance/folder
# when the app instance is created.
#
# The app.config.from_pyfile('config.py')
#  connects to the config.py file and all its
# contents are appended to the app.config.