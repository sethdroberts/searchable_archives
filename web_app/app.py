from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

# To run in debug mode, enter: flask run --debug