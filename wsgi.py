# wsgi.py
from flask import Flask, jsonify
app = Flask(__name__)


PRODUCTS = [
    {'id': 1, 'name': 'Skello'},
    {'id': 2, 'name': 'Socialive.tv'},
    {'id': 3, 'name': 'Twitter'}
]

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    return jsonify(PRODUCTS) 

@app.route('/api/v1/products/<int:id>')
def read(id):
    try:
        return jsonify(PRODUCTS[id-1])
    except:
        return 'Product key ' + str(id) + ' does not exist!'
