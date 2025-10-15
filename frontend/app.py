from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Use environment variable for Docker, fallback to localhost for local development
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5002")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    car_data = {
        "model_year": int(request.form["model_year"]),
        "age": int(request.form["age"]),
        "fuel_type": request.form["fuel_type"],
        "transmission": request.form["transmission"],
        "clean_title": int(request.form["clean_title"]),
    }

    try:
        # Call backend API
        response = requests.get(f"{BACKEND_URL}/precio_actual", params=car_data, timeout=5)
        if response.ok:
            result = response.json()
        else:
            result = None
            error = f"API Error: {response.status_code}"
            return render_template("index.html", error=error, car_data=car_data)

        return render_template("index.html", result=result, car_data=car_data)
    except Exception as e:
        return render_template("index.html", error=str(e), car_data=car_data)


@app.route("/predict_future", methods=["POST"])
def predict_future():
    # Get form data
    car_data = {
        "model_year": int(request.form["model_year"]),
        "age": int(request.form["age"]),
        "fuel_type": request.form["fuel_type"],
        "transmission": request.form["transmission"],
        "clean_title": int(request.form["clean_title"]),
        "meses": 12,
    }

    try:
        # Call backend API
        response = requests.get(f"{BACKEND_URL}/prediccion_futura", params=car_data, timeout=5)
        if response.ok:
            future_result = response.json()
        else:
            future_result = None
            error = f"API Error: {response.status_code}"
            return render_template("index.html", error=error, car_data=car_data)

        return render_template("index.html", future_result=future_result, car_data=car_data)
    except Exception as e:
        return render_template("index.html", error=str(e), car_data=car_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
