import unittest
from unittest.mock import patch
from app import create_app

class TestProductEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    @patch('app.services.product_service.get_all_products')
    def test_get_all_products(self, mock_get_all_products):
        mock_get_all_products.return_value = [
            {"id": 1, "name": "Widget", "price": 25.50},
            {"id": 2, "name": "Gadget", "price": 50.00}
        ]
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json["products"]), 2)

    @patch('app.services.product_service.create_product')
    def test_create_product(self, mock_create_product):
        mock_create_product.return_value = {"id": 3, "name": "Thingamajig", "price": 75.00}
        data = {"name": "Thingamajig", "price": 75.00}
        response = self.client.post('/products/', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], "Thingamajig")

    @patch('app.services.product_service.get_product_by_id')
    def test_get_product_not_found(self, mock_get_product_by_id):
        mock_get_product_by_id.return_value = None
        response = self.client.get('/products/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "Product not found")
