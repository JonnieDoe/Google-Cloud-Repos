try:
    import logging
    import flask
except Exception as err:
    logging.log(logging.ERROR, "Error on importing modules: {error}".format(error=str(err.message)))
    raise err


"""
Define the app object
    Define template and static folder by hand
    Load config from Instance folders --> instance_relative_config=True

app = Flask(__name__, template_folder="templates", static_folder="static", instance_path='/absolute/path/to/instance/folder')
"""
app = flask.Flask(__name__, template_folder="templates", static_folder="static", instance_relative_config=True)

# Load the default configuration
# Now we can access the configuration variables via app.config["VAR_NAME"]
app.config.from_object('config.development')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py', silent=True)

#import functions
import errors
import gae_tasks
