# wsgi.py
from flask import Flask, jsonify, abort, render_template, request, make_response
app = Flask(__name__)


PRODUCTS = [
    {'id': 2, 'name': 'Socialive.tv'},
    {'id': 3, 'name': 'Twitter'},
    {'id': 1, 'name': 'Skello'}
]

PRODUCTS_MAP = {
    item['id']: item
    for item in PRODUCTS
}

@app.route('/')
def hello():
    return "Hello World!"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/api/v1/products')
def get_products():
    return jsonify(PRODUCTS) 

@app.route('/api/v1/products/<int:id>')
def get_product(id):
    result = PRODUCTS_MAP.get(id)
    if result:
        return jsonify(result)
    abort(404)

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def del_product(id):
    result = PRODUCTS_MAP.get(id)
    if result:
        del PRODUCTS_MAP[id]
        return jsonify(PRODUCTS_MAP)
        make_response('Item deleted', 200)
    abort(404)
