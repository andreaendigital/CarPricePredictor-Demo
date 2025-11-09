from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import math
import json
import os
import time
import psutil
from datetime import datetime
import urllib3
from dotenv import load_dotenv
import threading
import random

# Disable SSL warnings for Splunk Cloud
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend connections

# Monitoring variables
start_time = time.time()
request_count = 0
prediction_count = 0

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
        import requests

        headers = {"X-SF-Token": SPLUNK_TOKEN, "Content-Type": "application/json"}

        if dimensions is None:
            dimensions = {}

        # Add default dimensions
        dimensions.update({"service": "car-price-backend", "environment": "development", "host": "localhost"})

        payload = {
            "gauge": [{"metric": metric_name, "value": value, "dimensions": dimensions, "timestamp": int(time.time() * 1000)}]
        }

        response = requests.post(SPLUNK_URL, json=payload, headers=headers, timeout=5)
        if response.status_code != 200:
            print(f"❌ Splunk error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Splunk error: {e}")


def send_continuous_metrics():
    """Send continuous system and business metrics to Splunk Observability Cloud"""
    while continuous_monitoring:
        try:
            # System Performance Metrics
            send_to_splunk_observability("car_price.system.cpu_percent", psutil.cpu_percent())
            send_to_splunk_observability("car_price.system.memory_percent", psutil.virtual_memory().percent)
            send_to_splunk_observability("car_price.system.disk_usage", psutil.disk_usage("/").percent)

            # Application Metrics
            uptime = time.time() - start_time
            send_to_splunk_observability("car_price.app.uptime_seconds", uptime)
            send_to_splunk_observability("car_price.app.total_requests", request_count)
            send_to_splunk_observability("car_price.app.total_predictions", prediction_count)

            # Business KPIs (simulated realistic values)
            send_to_splunk_observability("car_price.business.avg_prediction_value", random.uniform(15000, 45000))
            send_to_splunk_observability("car_price.business.model_accuracy", random.uniform(0.85, 0.95))
            send_to_splunk_observability("car_price.business.active_users", random.randint(5, 25))

            time.sleep(10)  # Send metrics every 10 seconds
        except Exception as e:
            print(f"❌ Continuous metrics error: {e}")
            time.sleep(10)


# Start continuous monitoring thread
monitoring_thread = threading.Thread(target=send_continuous_metrics, daemon=True)
monitoring_thread.start()

# === Cargar modelo entrenado ===
model_path = os.environ.get("MODEL_PATH", "modelo/modelo.joblib")
try:
    modelo = joblib.load(model_path)
except FileNotFoundError:
    print(f"Warning: ML model not found at {model_path}, using fallback prediction")
    modelo = None

# === Configuración de almacenamiento de vehículos ===
DB_FILE = os.environ.get("DB_PATH", "vehiculos.json")
if not os.path.exists(DB_FILE):
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, "w") as f:
        json.dump([], f)


# === Funciones auxiliares basadas en el notebook ===
def predict_price(data: dict):
    """Predice el precio actual del vehículo usando el modelo entrenado."""
    try:
        if modelo is not None:
            df = pd.DataFrame([data])
            pred = modelo.predict(df)[0]
            return float(pred)
    except Exception as e:
        print(f"ML model error: {e}, using fallback")

    # Fallback calculation
    base_price = 15000 + (data["model_year"] - 2000) * 500 - data["age"] * 800
    fuel_bonus = {"Electric": 3000, "Hybrid": 1500, "Gasoline": 0, "Diesel": -500}.get(data["fuel_type"], 0)
    trans_bonus = 500 if data["transmission"] == "Automatic" else 0
    title_bonus = 1000 if data["clean_title"] == 1 else -2000
    return max(base_price + fuel_bonus + trans_bonus + title_bonus, 5000)


def predict_future_price(current_price, months_ahead=12, k_rate=None):
    """Proyecta el precio futuro aplicando depreciación exponencial."""
    if current_price <= 0:
        return 0.0
    if k_rate is None:
        yearly = 0.10  # depreciación anual base
    else:
        yearly = k_rate
    years = months_ahead / 12.0
    future_price = current_price * math.exp(-yearly * years)
    return float(future_price)


@app.route("/")
def home():
    return jsonify(
        {
            "message": "API de predicción y publicación de vehículos (basado en tu modelo joblib)",
            "endpoints": {
                "GET /current_value_market": "Predice el precio actual del vehículo",
                "GET /future_prediction": "Predice el precio futuro del vehículo en N meses",
                "POST /publish_car": "Permite publicar un vehículo en venta",
                "GET /health": "Health check endpoint",
                "GET /dashboard": "Real-time monitoring dashboard",
                "GET /metrics/json": "JSON metrics API",
            },
        }
    )


# First Endpoint GET - Get for current car price


@app.route("/current_value_market", methods=["GET"])
def current_value_market():
    try:
        # Obtener y validar parámetros
        model_year = request.args.get("model_year")
        age = request.args.get("age")
        fuel_type = request.args.get("fuel_type")
        transmission = request.args.get("transmission")
        clean_title = request.args.get("clean_title")

        # Validar que no sean None
        if not all([model_year, age, fuel_type, transmission, clean_title]):
            return (
                jsonify(
                    {
                        "error": "Faltan parámetros requeridos",
                        "requeridos": [
                            "model_year",
                            "age",
                            "fuel_type",
                            "transmission",
                            "clean_title",
                        ],
                    }
                ),
                400,
            )

        data = {
            "model_year": float(model_year),
            "age": float(age),
            "fuel_type": fuel_type,
            "transmission": transmission,
            "clean_title": float(clean_title),
        }

        global prediction_count
        prediction_count += 1

        # Send metrics to Splunk Observability Cloud
        send_to_splunk_observability(
            "car_price.predictions.current_value",
            1,
            {"fuel_type": fuel_type, "transmission": transmission, "endpoint": "current_value_market"},
        )
        send_to_splunk_observability("car_price.system.cpu_percent", psutil.cpu_percent())
        send_to_splunk_observability("car_price.system.memory_percent", psutil.virtual_memory().percent)
        send_to_splunk_observability("car_price.requests.total", prediction_count)

        pred = predict_price(data)
        return jsonify({"datos": data, "current_value_market_estimado": round(pred, 2)})
    except ValueError as e:
        return jsonify({"error": f"Error de conversión: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Second Endpoint, This is a GET for a future price


@app.route("/future_prediction", methods=["GET"])
def future_prediction():
    try:
        meses = int(request.args.get("meses", 12))

        # Obtener y validar parámetros
        model_year = request.args.get("model_year")
        age = request.args.get("age")
        fuel_type = request.args.get("fuel_type")
        transmission = request.args.get("transmission")
        clean_title = request.args.get("clean_title")

        if not all([model_year, age, fuel_type, transmission, clean_title]):
            return (
                jsonify(
                    {
                        "error": "Faltan parámetros requeridos",
                        "requeridos": [
                            "model_year",
                            "age",
                            "fuel_type",
                            "transmission",
                            "clean_title",
                        ],
                    }
                ),
                400,
            )

        data = {
            "model_year": float(model_year),
            "age": float(age),
            "fuel_type": fuel_type,
            "transmission": transmission,
            "clean_title": float(clean_title),
        }

        global prediction_count
        prediction_count += 1

        # Send metrics to Splunk Observability Cloud
        send_to_splunk_observability(
            "car_price.predictions.future_value",
            1,
            {
                "fuel_type": fuel_type,
                "transmission": transmission,
                "months_ahead": str(meses),
                "endpoint": "future_prediction",
            },
        )
        send_to_splunk_observability("car_price.business.months_forecast", meses)
        send_to_splunk_observability("car_price.requests.total", prediction_count)

        pred_actual = predict_price(data)
        pred_futura = predict_future_price(pred_actual, months_ahead=meses)

        return jsonify(
            {
                "datos": data,
                "meses": meses,
                "current_value_market_estimado": round(pred_actual, 2),
                "precio_estimado_futuro": round(pred_futura, 2),
            }
        )
    except ValueError as e:
        return jsonify({"error": f"Error de conversión: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# === Endpoint 3: publish car ===
@app.route("/publish_car", methods=["POST"])
def publish_car():
    try:
        data = request.get_json()

        campos = [
            "model_year",
            "age",
            "fuel_type",
            "transmission",
            "clean_title",
            "precio",
        ]
        if not all(campo in data for campo in campos):
            return jsonify({"error": f"Faltan campos: {', '.join(campos)}"}), 400

        # Leer base
        with open(DB_FILE, "r") as f:
            vehiculos = json.load(f)

        nuevo_id = len(vehiculos) + 1
        data["id"] = nuevo_id

        vehiculos.append(data)
        with open(DB_FILE, "w") as f:
            json.dump(vehiculos, f, indent=4)

        # Calcular precio recomendado con el modelo
        pred = predict_price(
            {
                "model_year": float(data["model_year"]),
                "age": float(data["age"]),
                "fuel_type": data["fuel_type"],
                "transmission": data["transmission"],
                "clean_title": float(data["clean_title"]),
            }
        )

        return (
            jsonify(
                {
                    "message": "Vehículo publicado con éxito",
                    "vehiculo_id": nuevo_id,
                    "precio_publicado": data["precio"],
                    "precio_recomendado_modelo": round(pred, 2),
                    "datos": data,
                }
            ),
            201,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/dashboard")
def dashboard():
    uptime = time.time() - start_time
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🔧 Backend API - Monitoring</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body {{ font-family: Arial; margin: 40px; background: #2c3e50; color: white; }}
            .metric {{ background: #34495e; padding: 20px; margin: 10px 0; border-radius: 8px; }}
            .value {{ font-size: 2em; font-weight: bold; color: #3498db; }}
            .label {{ color: #bdc3c7; margin-top: 5px; }}
            .splunk {{ background: #e67e22; padding: 10px; margin: 10px 0; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>🔧 Backend API Monitoring (Port 5002)</h1>
        <div class="metric">
            <div class="value">{request_count}</div>
            <div class="label">Total API Requests</div>
        </div>
        <div class="metric">
            <div class="value">{prediction_count}</div>
            <div class="label">ML Predictions Made</div>
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
            "service": "backend-api",
            "port": 5002,
            "timestamp": datetime.now().isoformat(),
            "uptime_seconds": uptime,
            "requests_total": request_count,
            "predictions_total": prediction_count,
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
            "service": "backend-api",
            "timestamp": datetime.now().isoformat(),
            "model_loaded": modelo is not None,
            "splunk_observability": f"https://app.{SPLUNK_REALM}.signalfx.com",
        }
    )


if __name__ == "__main__":
    host = os.getenv("BACKEND_HOST", "0.0.0.0")
    port = int(os.getenv("BACKEND_PORT", "5002"))
    debug = os.getenv("BACKEND_DEBUG", "true").lower() == "true"
    app.run(debug=debug, host=host, port=port)
