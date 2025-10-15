import os
import sys
import unittest

# Add frontend directory to path for imports
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
sys.path.insert(0, frontend_dir)

# Import after path modification
from app import app  # noqa: E402


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_home_page(self):
        """Test that the home page loads"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Car Price Predictor", response.data)

    def test_predict_endpoint_exists(self):
        """Test that predict endpoint exists (will fail without backend)"""
        response = self.client.post(
            "/predict",
            data={"model_year": "2020", "age": "4", "fuel_type": "Gasoline", "transmission": "Automatic", "clean_title": "1"},
        )
        # Should return 200 even if backend is down (error handling)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
