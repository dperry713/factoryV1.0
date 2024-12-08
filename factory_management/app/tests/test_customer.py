import unittest
from app.models import Customer
from app.extensions import db

class TestCustomerModel(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(name='John Doe')

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'John Doe')

    def test_customer_persistence(self):
        db.session.add(self.customer)
        db.session.commit()
        self.assertIsNotNone(self.customer.id)

if __name__ == '__main__':
    unittest.main()