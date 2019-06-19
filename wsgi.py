# wsgi.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/product')
def product():
    return "No product at least..."

@app.route('/api/v1/products')
def products():
    PRODUCTS = [
        {'id': 1, 'name': 'Skello'},
        {'id': 2, 'name': 'Socialive.tv'},
        {'id': 3, 'name': 'Twitter'}
    ]
    return jsonify(PRODUCTS) 
