# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_products_unknown(self):
        response = self.client.get("/api/v1/products/4")
        products = response.json
        print(products, '404')

    def test_products_delete(self):
        response = self.client.delete("/api/v1/products/2")
        answer = response.json
        print(answer)
