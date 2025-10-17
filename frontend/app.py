"""Flask frontend application for Car Price Predictor.

Provides a web interface for vehicle price prediction and publishing.
Integrates with backend ML API for predictions.
"""

import os
from typing import Dict, Any, Optional, Tuple

import requests
from flask import Flask, render_template, request
from requests.exceptions import RequestException, Timeout

# Configuration constants
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5002")
API_TIMEOUT = 10
DEFAULT_MONTHS = 12

# Form validation constants
MIN_YEAR = 1990
MAX_YEAR = 2024
MIN_AGE = 0
MAX_AGE = 50
MIN_PRICE = 1000

app = Flask(__name__)


def extract_vehicle_data(form_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract and validate vehicle data from form.

    Args:
        form_data: Raw form data from request

    Returns:
        Validated vehicle data dictionary

    Raises:
        ValueError: If data validation fails
    """
    try:
        return {
            "model_year": int(form_data["model_year"]),
            "age": int(form_data["age"]),
            "fuel_type": form_data["fuel_type"],
            "transmission": form_data["transmission"],
            "clean_title": int(form_data["clean_title"]),
        }
    except (KeyError, ValueError) as e:
        raise ValueError(f"Invalid form data: {e}") from e


def call_backend_api(
    endpoint: str, data: Dict[str, Any], method: str = "GET"
) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """Make API call to backend service.

    Args:
        endpoint: API endpoint path
        data: Request data
        method: HTTP method (GET or POST)

    Returns:
        Tuple of (response_data, error_message)
    """
    url = f"{BACKEND_URL}/{endpoint}"

    try:
        if method == "GET":
            response = requests.get(url, params=data, timeout=API_TIMEOUT)
        else:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)

        if response.ok:
            return response.json(), None
        else:
            return None, f"API Error: {response.status_code}"

    except Timeout:
        return None, "Request timeout - backend service unavailable"
    except RequestException as e:
        return None, f"Connection error: {str(e)}"
    except Exception as e:
        return None, f"Unexpected error: {str(e)}"


@app.route("/")
def index() -> str:
    """Render main application page."""
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict() -> str:
    """Handle current price prediction requests."""
    try:
        car_data = extract_vehicle_data(request.form)
        result, error = call_backend_api("current_value_market", car_data)

        return render_template("index.html", result=result, error=error, car_data=car_data, active_tab="tab1")

    except ValueError as e:
        return render_template("index.html", error=str(e), active_tab="tab1")


@app.route("/predict_future", methods=["POST"])
def predict_future() -> str:
    """Handle future price prediction requests."""
    try:
        car_data = extract_vehicle_data(request.form)
        car_data["meses"] = DEFAULT_MONTHS

        future_result, error = call_backend_api("future_prediction", car_data)

        return render_template("index.html", future_result=future_result, error=error, car_data=car_data, active_tab="tab2")

    except ValueError as e:
        return render_template("index.html", error=str(e), active_tab="tab2")


@app.route("/publish", methods=["POST"])
def publish_vehicle() -> str:
    """Handle vehicle publishing requests."""
    try:
        vehicle_data = extract_vehicle_data(request.form)
        vehicle_data["precio"] = float(request.form["precio"])

        publish_result, error = call_backend_api("publish_car", vehicle_data, method="POST")

        return render_template(
            "index.html", publish_result=publish_result, error=error, vehicle_data=vehicle_data, active_tab="tab3"
        )

    except ValueError as e:
        return render_template("index.html", error=str(e), active_tab="tab3")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
