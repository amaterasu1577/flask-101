# wsgi.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/product')
def product():
    return "No product at least..."
