import unittest
from datetime import date
from app.models import Production, Product
from app.extensions import db

class TestProductionModel(unittest.TestCase):
    def setUp(self):
        self.product = Product(name='Gadget', price=29.99)
        db.session.add(self.product)
        db.session.commit()
        self.production = Production(product_id=self.product.id, date=date.today())

    def test_production_creation(self):
        self.assertEqual(self.production.date, date.today())

    def test_production_persistence(self):
        db.session.add(self.production)
        db.session.commit()
        self.assertIsNotNone(self.production.id)

if __name__ == '__main__':
    unittest.main()