import unittest
from unittest.mock import patch
from app import create_app

class TestEmployeeEndpoints(unittest.TestCase):
    def setUp(self):
        """Set up the test client and context"""
        self.app = create_app()
        self.client = self.app.test_client()

    @patch('app.services.employee_service.get_all_employees')
    def test_get_all_employees(self, mock_get_all_employees):
        """Test getting all employees."""
        mock_get_all_employees.return_value = [
            {"id": 1, "name": "Alice", "position": "Manager"},
            {"id": 2, "name": "Bob", "position": "Engineer"}
        ]
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.json[0]["name"], "Alice")

    @patch('app.services.employee_service.create_employee')
    def test_create_employee(self, mock_create_employee):
        """Test creating a new employee."""
        mock_create_employee.return_value = {"id": 3, "name": "Charlie", "position": "Technician"}
        data = {"name": "Charlie", "position": "Technician"}
        response = self.client.post('/employees/', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], "Charlie")

    @patch('app.services.employee_service.get_employee_by_id')
    def test_get_employee_not_found(self, mock_get_employee_by_id):
        """Test getting an employee that does not exist."""
        mock_get_employee_by_id.return_value = None
        response = self.client.get('/employees/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "Employee not found")
