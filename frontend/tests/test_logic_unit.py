import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.data_processor import get_current_value  # noqa: E402
from logic.predictor import get_predictions  # noqa: E402


class TestLogicUnit(unittest.TestCase):
    def test_get_current_value(self):
        result = get_current_value()
        self.assertIsInstance(result, dict)

    def test_get_predictions_no_data(self):
        result = get_predictions()
        self.assertIsInstance(result, dict)
        self.assertIn("error", result)

    def test_get_predictions_missing_feature(self):
        result = get_predictions({"model_year": 2020})
        self.assertIn("error", result)

    def test_get_predictions_valid_data(self):
        data = {"model_year": 2020, "age": 4, "fuel_type": "Gasoline", "transmission": "Automatic", "clean_title": "Yes"}
        result = get_predictions(data)
        self.assertIn("predicted_price", result)
        self.assertIn("input_features", result)
        self.assertIn("model", result)
