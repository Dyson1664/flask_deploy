from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/page1')
def page1():
    return 'This is page 1!'

# @app.route('/caps')
# def caps(name=None):
#     return render_template('caps.html', name=name)