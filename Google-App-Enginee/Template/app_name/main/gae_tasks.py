import flask
from functools import wraps
from google.appengine.api.taskqueue import Task


__author__ = "DC"
__version__ = "0.1"


# Check if Task
def is_task(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if flask.request.headers.get("X-AppEngine-QueueName", None):
            # result = f(*args, **kwargs)
            # return result
            f(*args, **kwargs)
            return flask.make_response("Success", 200)
        else:
            flask.abort(403)

    return decorated_function


#################################################################################################
# Function to create A GAE Task
def create_task(url, method, params, queue_name="default"):
    task = Task(url=url, method=method, params=params)
    task.add(queue_name=queue_name)
