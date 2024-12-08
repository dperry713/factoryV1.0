import unittest
from app.models import Order, Product, Customer
from app.extensions import db

class TestOrderModel(unittest.TestCase):
    def setUp(self):
        self.product = Product(name='Widget', price=19.99)
        self.customer = Customer(name='Jane Doe')
        db.session.add(self.product)
        db.session.add(self.customer)
        db.session.commit()
        self.order = Order(product_id=self.product.id, customer_id=self.customer.id, quantity=3)

    def test_order_creation(self):
        self.assertEqual(self.order.quantity, 3)

    def test_order_persistence(self):
        db.session.add(self.order)
        db.session.commit()
        self.assertIsNotNone(self.order.id)

if __name__ == '__main__':
    unittest.main()