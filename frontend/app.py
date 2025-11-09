"""Flask frontend application for Car Price Predictor.

Provides a web interface for vehicle price prediction and publishing.
Integrates with backend ML API for predictions.
"""

import os
import time
import psutil
from datetime import datetime
import urllib3
from typing import Dict, Any, Optional, Tuple
import threading
import random

# Disable SSL warnings for Splunk Cloud
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
from flask import Flask, render_template, request, jsonify
from requests.exceptions import RequestException, Timeout
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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

# Monitoring variables
start_time = time.time()
request_count = 0
prediction_requests = 0
publish_requests = 0

# Continuous monitoring flag
continuous_monitoring = True

# Splunk Observability Cloud Configuration
SPLUNK_TOKEN = "PZuf3J0L2Op_Qj9hpAJzlw"
SPLUNK_REALM = "us1"
SPLUNK_URL = f"https://ingest.{SPLUNK_REALM}.signalfx.com/v2/datapoint"


@app.before_request
def count_requests():
    global request_count
    request_count += 1


def send_to_splunk_observability(metric_name, value, dimensions=None):
    """Send metrics to Splunk Observability Cloud"""
    try:
        headers = {"X-SF-Token": SPLUNK_TOKEN, "Content-Type": "application/json"}

        if dimensions is None:
            dimensions = {}

        # Add default dimensions
        dimensions.update({"service": "car-price-frontend", "environment": "development", "host": "localhost"})

        payload = {
            "gauge": [{"metric": metric_name, "value": value, "dimensions": dimensions, "timestamp": int(time.time() * 1000)}]
        }

        response = requests.post(SPLUNK_URL, json=payload, headers=headers, timeout=5)
        if response.status_code != 200:
            print(f"❌ Splunk error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Splunk error: {e}")


def send_continuous_metrics():
    """Send continuous frontend metrics to Splunk Observability Cloud"""
    while continuous_monitoring:
        try:
            # System Performance Metrics
            send_to_splunk_observability("car_price.frontend.cpu_percent", psutil.cpu_percent())
            send_to_splunk_observability("car_price.frontend.memory_percent", psutil.virtual_memory().percent)

            # Application Metrics
            uptime = time.time() - start_time
            send_to_splunk_observability("car_price.frontend.uptime_seconds", uptime)
            send_to_splunk_observability("car_price.frontend.total_requests", request_count)
            send_to_splunk_observability("car_price.frontend.prediction_requests", prediction_requests)
            send_to_splunk_observability("car_price.frontend.publish_requests", publish_requests)

            # User Experience Metrics (simulated)
            send_to_splunk_observability("car_price.frontend.page_load_time", random.uniform(0.5, 2.0))
            send_to_splunk_observability("car_price.frontend.user_satisfaction", random.uniform(4.0, 5.0))
            send_to_splunk_observability("car_price.frontend.conversion_rate", random.uniform(0.15, 0.35))

            time.sleep(10)  # Send metrics every 10 seconds
        except Exception as e:
            print(f"❌ Frontend continuous metrics error: {e}")
            time.sleep(10)


# Start continuous monitoring thread
monitoring_thread = threading.Thread(target=send_continuous_metrics, daemon=True)
monitoring_thread.start()


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
    global prediction_requests
    prediction_requests += 1

    # Send metrics to Splunk Observability Cloud
    send_to_splunk_observability(
        "car_price.frontend.predictions", 1, {"user_ip": request.remote_addr or "unknown", "action": "current_prediction"}
    )
    send_to_splunk_observability("car_price.frontend.requests.total", prediction_requests)

    try:
        car_data = extract_vehicle_data(request.form)
        result, error = call_backend_api("current_value_market", car_data)

        return render_template("index.html", result=result, error=error, car_data=car_data, active_tab="tab1")

    except ValueError as e:
        return render_template("index.html", error=str(e), active_tab="tab1")


@app.route("/predict_future", methods=["POST"])
def predict_future() -> str:
    """Handle future price prediction requests."""
    global prediction_requests
    prediction_requests += 1

    # Send metrics to Splunk Observability Cloud
    send_to_splunk_observability(
        "car_price.frontend.predictions", 1, {"user_ip": request.remote_addr or "unknown", "action": "future_prediction"}
    )
    send_to_splunk_observability("car_price.frontend.requests.total", prediction_requests)

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
    global publish_requests
    publish_requests += 1

    # Send metrics to Splunk Observability Cloud
    send_to_splunk_observability(
        "car_price.frontend.publishes", 1, {"user_ip": request.remote_addr or "unknown", "action": "vehicle_publish"}
    )
    send_to_splunk_observability("car_price.frontend.publish.total", publish_requests)

    try:
        vehicle_data = extract_vehicle_data(request.form)
        vehicle_data["precio"] = float(request.form["precio"])

        publish_result, error = call_backend_api("publish_car", vehicle_data, method="POST")

        return render_template(
            "index.html", publish_result=publish_result, error=error, vehicle_data=vehicle_data, active_tab="tab3"
        )

    except ValueError as e:
        return render_template("index.html", error=str(e), active_tab="tab3")


@app.route("/dashboard")
def dashboard():
    uptime = time.time() - start_time
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🌐 Frontend Web - Monitoring</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body {{ font-family: Arial; margin: 40px; background: #8e44ad; color: white; }}
            .metric {{ background: #9b59b6; padding: 20px; margin: 10px 0; border-radius: 8px; }}
            .value {{ font-size: 2em; font-weight: bold; color: #ecf0f1; }}
            .label {{ color: #ecf0f1; margin-top: 5px; }}
            .splunk {{ background: #e67e22; padding: 10px; margin: 10px 0; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>🌐 Frontend Web Monitoring (Port 3000)</h1>
        <div class="metric">
            <div class="value">{request_count}</div>
            <div class="label">Total Web Requests</div>
        </div>
        <div class="metric">
            <div class="value">{prediction_requests}</div>
            <div class="label">Prediction Requests</div>
        </div>
        <div class="metric">
            <div class="value">{publish_requests}</div>
            <div class="label">Publish Requests</div>
        </div>
        <div class="metric">
            <div class="value">{cpu_usage:.1f}%</div>
            <div class="label">CPU Usage</div>
        </div>
        <div class="metric">
            <div class="value">{memory_usage:.1f}%</div>
            <div class="label">Memory Usage</div>
        </div>
        <div class="metric">
            <div class="value">{int(uptime//3600)}h {int((uptime%3600)//60)}m</div>
            <div class="label">Uptime</div>
        </div>
        <div class="splunk">
            <strong>📊 Splunk Observability:</strong> <a href="https://app.us1.signalfx.com" target="_blank" style="color: white;">View Dashboards</a>
        </div>
    </body>
    </html>
    """


@app.route("/metrics/json")
def metrics_json():
    uptime = time.time() - start_time
    return jsonify(
        {
            "service": "frontend-web",
            "port": 3000,
            "timestamp": datetime.now().isoformat(),
            "uptime_seconds": uptime,
            "requests_total": request_count,
            "prediction_requests": prediction_requests,
            "publish_requests": publish_requests,
            "system": {"cpu_percent": psutil.cpu_percent(), "memory_percent": psutil.virtual_memory().percent},
            "status": "healthy",
            "splunk_observability": True,
        }
    )


@app.route("/health")
def health_check():
    return jsonify(
        {
            "status": "healthy",
            "service": "frontend-web",
            "timestamp": datetime.now().isoformat(),
            "backend_url": BACKEND_URL,
            "splunk_observability": f"https://app.{SPLUNK_REALM}.signalfx.com",
        }
    )


if __name__ == "__main__":
    host = os.getenv("FRONTEND_HOST", "0.0.0.0")
    port = int(os.getenv("FRONTEND_PORT", "3000"))
    debug = os.getenv("FRONTEND_DEBUG", "true").lower() == "true"
    app.run(debug=debug, host=host, port=port)
