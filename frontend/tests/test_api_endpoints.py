import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app  # noqa: E402


class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_valoractual_endpoint(self):
        test_data = {
            "model_year": 2020,
            "age": 4,
            "fuel_type": "Gasoline",
            "transmission": "Automatic",
            "clean_title": "Yes",
        }
        response = self.client.post("/valoractual", json=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("current_market_value", response.get_json())

    def test_predictions_endpoint(self):
        test_data = {
            "model_year": 2020,
            "age": 4,
            "fuel_type": "Gasoline",
            "transmission": "Automatic",
            "clean_title": "Yes",
        }
        response = self.client.post("/predictions", json=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("predicted_price", response.get_json())
