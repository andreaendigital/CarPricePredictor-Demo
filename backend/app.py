from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import math
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend connections

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
                "GET /precio_actual": "Predice el precio actual del vehículo",
                "GET /prediccion_futura": "Predice el precio futuro del vehículo en N meses",
                "POST /publicar_vehiculo": "Permite publicar un vehículo en venta",
            },
        }
    )


# First Endpoint GET - Get for current car price

@app.route("/precio_actual", methods=["GET"])
def precio_actual():
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

        pred = predict_price(data)
        return jsonify({"datos": data, "precio_actual_estimado": round(pred, 2)})
    except ValueError as e:
        return jsonify({"error": f"Error de conversión: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Second Endpoint, This is a GET for a future price

@app.route("/prediccion_futura", methods=["GET"])
def prediccion_futura():
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

        pred_actual = predict_price(data)
        pred_futura = predict_future_price(pred_actual, months_ahead=meses)

        return jsonify(
            {
                "datos": data,
                "meses": meses,
                "precio_actual_estimado": round(pred_actual, 2),
                "precio_estimado_futuro": round(pred_futura, 2),
            }
        )
    except ValueError as e:
        return jsonify({"error": f"Error de conversión: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# === Endpoint 3: publicar vehículo ===
@app.route("/publicar_vehiculo", methods=["POST"])
def publicar_vehiculo():
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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
