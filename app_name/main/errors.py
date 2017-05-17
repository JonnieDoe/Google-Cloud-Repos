import time
from datetime import datetime
from main import flask, app


__author__ = "DC"
__version__ = "0.1"


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.template_filter('time')
def timectime():
    return time.time()


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('errors/404.html'), 404


@app.errorhandler(403)
def unauthorized(e):
    return flask.render_template('errors/403.html'), 403
