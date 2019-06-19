# wsgi.py
from flask import Flask, jsonify, abort, render_template, request, make_response
app = Flask(__name__)


class Counter:
    def __init__(self):
        self.id = 3

    def next(self):
        self.id += 1
        return self.id
    
    def prev(self):
        self.id -= 1
        return self.id

ID = Counter()

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
    return jsonify(PRODUCTS_MAP) 

@app.route('/api/v1/products/<int:id>')
def get_product(id):
    if id in PRODUCTS_MAP:
        return jsonify(PRODUCTS_MAP[id])
    abort(404)

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def del_product(id):
    if id in PRODUCTS_MAP:
        del PRODUCTS_MAP[id]
        return jsonify(PRODUCTS_MAP)
    abort(404)

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    index = ID.next()
    body = request.get_json()
    PRODUCTS_MAP.update({index: {'id': index, 'name': body['name']}})
    return jsonify(PRODUCTS_MAP)

@app.route('/api/v1/products/<int:id>', methods=['PATCH'])
def patch_product(id):
    if id in PRODUCTS_MAP:
        body = request.get_json()
        PRODUCTS_MAP.update({id: {'id': id, 'name': body['name']}})
    return jsonify(PRODUCTS_MAP)
