from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """View function for root index page."""
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)
