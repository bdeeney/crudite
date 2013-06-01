import os.path

from flask import Flask, send_from_directory
from crudite.helpers import subscribe_logging_helpers
from crudite.testing import load

app = Flask(__name__)


@app.route('/')
def hello_world():
    """View function for root index page."""
    return 'Hello world!'


@app.route('/favicon.ico')
def favicon():
    """View function for favicon."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    import sys
    if '--verbose' in sys.argv:
        subscribe_logging_helpers(app)
    if '--load' in sys.argv:
        load('http://127.0.0.1:5000/')
    app.run(debug=True)
