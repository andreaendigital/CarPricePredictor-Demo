from flask import Flask
from flask_restx import Api, Resource, fields, reqparse
from flask_cors import CORS
import joblib
import pandas as pd
import math
import json
import os

# flask implementation
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Swagger API Configuration with Professional Styling
api = Api(
    app,
    version="1.0",
    title="🚗 Car Price Prediction API",
    description="Professional ML-Powered Vehicle Valuation System",
    doc="/docs/",
    contact="Development Team",
    contact_email="dev@carprice.com",
)


# Professional Documentation Routes
@app.route("/")
def index():
    """Redirect to documentation menu"""
    from flask import redirect

    return redirect("/docs-menu")


@app.route("/redoc")
def redoc():
    """ReDoc - Professional dark theme documentation"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚗 Car Price Prediction API - Professional Documentation</title>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            body {
                margin: 0; padding: 0;
                background: #263238;
                font-family: 'Inter', sans-serif;
            }
        </style>
    </head>
    <body>
        <div id="redoc-container"></div>
        <script src="https://cdn.jsdelivr.net/npm/redoc@2.0.0/bundles/redoc.standalone.js"></script>
        <script>
            Redoc.init('/swagger.json', {
                theme: {
                    colors: {
                        primary: {
                            main: '#667eea'
                        }
                    },
                    typography: {
                        fontFamily: 'Inter, sans-serif',
                        code: {
                            fontFamily: 'Monaco, Consolas, monospace'
                        }
                    }
                }
            }, document.getElementById('redoc-container'));
        </script>
    </body>
    </html>
    """


@app.route("/rapidoc")
def rapidoc():
    """RapiDoc - Modern interactive documentation"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Car Price Prediction API - RapiDoc</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>
    </head>
    <body>
        <rapi-doc
            spec-url="/swagger.json"
            theme="dark"
            bg-color="#14191f"
            text-color="#aec2e0"
            header-color="#197278"
            primary-color="#f76707"
            render-style="read"
            show-header="true"
            allow-try="true"
            allow-server-selection="false"
            show-info="true"
            show-components="true"
        >
        </rapi-doc>
    </body>
    </html>
    """


@app.route("/elements")
def elements():
    """Stoplight Elements - Professional API documentation"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Car Price Prediction API - Elements</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://unpkg.com/@stoplight/elements/styles.min.css">
    </head>
    <body>
        <elements-api
            apiDescriptionUrl="/swagger.json"
            router="hash"
            layout="sidebar"
            hideInternal="true"
        />
        <script src="https://unpkg.com/@stoplight/elements/web-components.min.js"></script>
    </body>
    </html>
    """


@app.route("/scalar")
def scalar():
    """Scalar - Modern beautiful API documentation"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Car Price Prediction API - Scalar</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
    </head>
    <body>
        <script id="api-reference" data-url="/swagger.json"></script>
        <script src="https://cdn.jsdelivr.net/npm/@scalar/api-reference"></script>
    </body>
    </html>
    """


@app.route("/docs-menu")
def docs_menu():
    """Documentation menu with all available options"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Car Price Prediction API - Documentation Hub</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0; padding: 40px; min-height: 100vh;
            }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: white; text-align: center; margin-bottom: 40px; font-size: 2.5em; }
            .docs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
            .doc-card {
                background: white; border-radius: 12px; padding: 30px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .doc-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 12px 40px rgba(0,0,0,0.15);
            }
            .doc-card h3 { color: #333; margin-bottom: 15px; font-size: 1.4em; }
            .doc-card p { color: #666; margin-bottom: 20px; line-height: 1.6; }
            .doc-link {
                display: inline-block; background: #667eea; color: white;
                padding: 12px 24px; border-radius: 6px; text-decoration: none;
                font-weight: 500; transition: background 0.3s ease;
            }
            .doc-link:hover { background: #5a67d8; }
            .badge {
                display: inline-block; background: #f7fafc; color: #4a5568;
                padding: 4px 8px; border-radius: 4px; font-size: 0.8em;
                margin-left: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚗 Car Price Prediction API</h1>
            <div class="docs-grid">
                <div class="doc-card">
                    <h3>Swagger UI <span class="badge">Interactive</span></h3>
                    <p>Interactive API documentation with "Try it out" functionality.
                    Perfect for testing endpoints directly in the browser.</p>
                    <a href="/docs/" class="doc-link">Open Swagger UI</a>
                </div>
                <div class="doc-card">
                    <h3>ReDoc <span class="badge">Beautiful</span></h3>
                    <p>Professional dark theme documentation with clean HTTP status codes and beautiful typography.</p>
                    <a href="/redoc" class="doc-link">Open ReDoc</a>
                </div>
                <div class="doc-card">
                    <h3>RapiDoc <span class="badge">Modern</span></h3>
                    <p>Modern interactive documentation with customizable themes and advanced features.</p>
                    <a href="/rapidoc" class="doc-link">Open RapiDoc</a>
                </div>
                <div class="doc-card">
                    <h3>Elements <span class="badge">Professional</span></h3>
                    <p>Stoplight Elements provides enterprise-grade API documentation with sidebar navigation.</p>
                    <a href="/elements" class="doc-link">Open Elements</a>
                </div>
                <div class="doc-card">
                    <h3>Scalar <span class="badge">Elegant</span></h3>
                    <p>Modern, elegant API documentation with beautiful design and smooth interactions.</p>
                    <a href="/scalar" class="doc-link">Open Scalar</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """


# Namespaces for organization
ns_prediction = api.namespace("prediction", description="Vehicle price prediction operations")
ns_vehicles = api.namespace("vehicles", description="Vehicle management operations")

# === Load ML Model ===
try:
    import warnings

    warnings.filterwarnings("ignore")
    modelo = joblib.load("modelo/modelo.joblib")
    print("ML model loaded successfully")
except Exception as e:
    print(f"Warning: Could not load ML model: {e}")
    modelo = None

# === Database Configuration ===
DB_FILE = "vehiculos.json"
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump([], f)

# === Data Models for Swagger ===
vehicle_input_model = api.model(
    "VehicleInput",
    {
        "model_year": fields.Integer(
            required=True,
            description="Vehicle manufacturing year (1990-2024)",
            min=1990,
            max=2024,
            example=2020,
        ),
        "age": fields.Integer(
            required=True,
            description="Vehicle age in years (0-50)",
            min=0,
            max=50,
            example=4,
        ),
        "fuel_type": fields.String(
            required=True,
            description="Fuel type",
            enum=["Gasoline", "Diesel", "Hybrid", "Electric"],
            example="Gasoline",
        ),
        "transmission": fields.String(
            required=True,
            description="Transmission type",
            enum=["Automatic", "Manual"],
            example="Automatic",
        ),
        "clean_title": fields.String(
            required=True,
            description="Clean title status",
            enum=["Yes", "No"],
            example="Yes",
        ),
    },
)

vehicle_listing_model = api.model(
    "VehicleListing",
    {
        "model_year": fields.Integer(
            required=True,
            description="Vehicle manufacturing year (1990-2024)",
            min=1990,
            max=2024,
            example=2020,
        ),
        "age": fields.Integer(
            required=True,
            description="Vehicle age in years (0-50)",
            min=0,
            max=50,
            example=5,
        ),
        "fuel_type": fields.String(
            required=True,
            description="Fuel type",
            enum=["Gasoline", "Diesel", "Hybrid", "Electric"],
            example="Gasoline",
        ),
        "transmission": fields.String(
            required=True,
            description="Transmission type",
            enum=["Automatic", "Manual"],
            example="Automatic",
        ),
        "clean_title": fields.String(
            required=True,
            description="Clean title status",
            enum=["Yes", "No"],
            example="Yes",
        ),
        "precio": fields.Float(
            required=True,
            description="Listed price in local currency",
            example=25000000,
        ),
    },
)

current_price_response = api.model(
    "CurrentPriceResponse",
    {
        "datos": fields.Nested(vehicle_input_model, description="Input vehicle data"),
        "precio_actual_estimado": fields.Float(description="Estimated current price", example=15750.50),
    },
)

future_price_response = api.model(
    "FuturePriceResponse",
    {
        "datos": fields.Nested(vehicle_input_model, description="Input vehicle data"),
        "meses": fields.Integer(description="Months ahead for prediction", example=24),
        "precio_actual_estimado": fields.Float(description="Current estimated price", example=15750.50),
        "precio_estimado_futuro": fields.Float(description="Future estimated price", example=12850.25),
    },
)

vehicle_listing_response = api.model(
    "VehicleListingResponse",
    {
        "message": fields.String(description="Success message", example="Vehículo publicado con éxito"),
        "vehiculo_id": fields.Integer(description="Generated vehicle ID", example=1),
        "precio_publicado": fields.Float(description="Published price", example=25000000),
        "precio_recomendado_modelo": fields.Float(description="ML model recommended price", example=22500000),
        "datos": fields.Raw(description="Complete vehicle data with ID"),
    },
)


# === Business Logic Functions ===
def predict_price(data: dict):
    """Predicts current vehicle price using trained ML model."""
    try:
        if modelo is None:
            raise Exception("Model not loaded")

        # Prepare data for ML model
        df = pd.DataFrame([data])

        # Suppress sklearn warnings
        import warnings

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            pred = modelo.predict(df)[0]

        return float(pred)

    except Exception as e:
        print(f"ML prediction failed: {e}, using fallback calculation")
        # Fallback calculation based on vehicle characteristics
        base_price = 15000 + (data["model_year"] - 2000) * 500 - data["age"] * 800

        # Adjust for fuel type
        fuel_multiplier = {
            "Electric": 1.3,
            "Hybrid": 1.1,
            "Gasoline": 1.0,
            "Diesel": 0.95,
        }.get(data["fuel_type"], 1.0)

        # Adjust for transmission
        trans_bonus = 500 if data["transmission"] == "Automatic" else 0

        # Adjust for clean title
        title_bonus = 1000 if data["clean_title"] == 1 else -2000

        final_price = (base_price * fuel_multiplier) + trans_bonus + title_bonus
        return max(final_price, 5000)


def predict_future_price(current_price, months_ahead=12, k_rate=None):
    """Projects future price using exponential depreciation model."""
    if current_price <= 0:
        return 0.0
    if k_rate is None:
        yearly = 0.10  # Base annual depreciation
    else:
        yearly = k_rate
    years = months_ahead / 12.0
    future_price = current_price * math.exp(-yearly * years)
    return float(future_price)


# === API Endpoints ===


@ns_prediction.route("/current-price")
class CurrentPrice(Resource):
    @api.doc("get_current_price")
    @api.expect(
        reqparse.RequestParser()
        .add_argument(
            "model_year",
            type=int,
            required=True,
            help="Vehicle manufacturing year (1990-2024)",
        )
        .add_argument("age", type=int, required=True, help="Vehicle age in years (0-50)")
        .add_argument(
            "fuel_type",
            type=str,
            required=True,
            help="Fuel type",
            choices=["Gasoline", "Diesel", "Hybrid", "Electric"],
        )
        .add_argument(
            "transmission",
            type=str,
            required=True,
            help="Transmission type",
            choices=["Automatic", "Manual"],
        )
        .add_argument(
            "clean_title",
            type=str,
            required=True,
            help="Clean title status",
            choices=["Yes", "No"],
        )
    )
    @api.marshal_with(current_price_response)
    def get(self):
        """Get current market value prediction for a vehicle"""
        parser = reqparse.RequestParser()
        parser.add_argument("model_year", type=int, required=True, choices=list(range(1990, 2025)))
        parser.add_argument("age", type=int, required=True, choices=list(range(0, 51)))
        parser.add_argument(
            "fuel_type",
            type=str,
            required=True,
            choices=["Gasoline", "Diesel", "Hybrid", "Electric"],
        )
        parser.add_argument("transmission", type=str, required=True, choices=["Automatic", "Manual"])
        parser.add_argument("clean_title", type=str, required=True, choices=["Yes", "No"])

        args = parser.parse_args()

        try:
            # Convert Yes/No to 1/0 for ML model
            clean_title_value = 1 if args["clean_title"] == "Yes" else 0

            data = {
                "model_year": args["model_year"],
                "age": args["age"],
                "fuel_type": args["fuel_type"],
                "transmission": args["transmission"],
                "clean_title": clean_title_value,
            }

            pred = predict_price(data)
            return {
                "datos": {
                    "model_year": args["model_year"],
                    "age": args["age"],
                    "fuel_type": args["fuel_type"],
                    "transmission": args["transmission"],
                    "clean_title": args["clean_title"],
                },
                "precio_actual_estimado": round(pred, 2),
            }
        except Exception as e:
            api.abort(400, f"Prediction error: {str(e)}")


@ns_prediction.route("/future-price")
class FuturePrice(Resource):
    @api.doc("get_future_price")
    @api.expect(
        reqparse.RequestParser()
        .add_argument(
            "model_year",
            type=int,
            required=True,
            help="Vehicle manufacturing year (1990-2024)",
        )
        .add_argument("age", type=int, required=True, help="Vehicle age in years (0-50)")
        .add_argument(
            "fuel_type",
            type=str,
            required=True,
            help="Fuel type",
            choices=["Gasoline", "Diesel", "Hybrid", "Electric"],
        )
        .add_argument(
            "transmission",
            type=str,
            required=True,
            help="Transmission type",
            choices=["Automatic", "Manual"],
        )
        .add_argument(
            "clean_title",
            type=str,
            required=True,
            help="Clean title status",
            choices=["Yes", "No"],
        )
        .add_argument(
            "meses",
            type=int,
            required=False,
            default=12,
            help="Months ahead for prediction (1-60)",
        )
    )
    @api.marshal_with(future_price_response)
    def get(self):
        """Get future price prediction for a vehicle"""
        parser = reqparse.RequestParser()
        parser.add_argument("model_year", type=int, required=True, choices=list(range(1990, 2025)))
        parser.add_argument("age", type=int, required=True, choices=list(range(0, 51)))
        parser.add_argument(
            "fuel_type",
            type=str,
            required=True,
            choices=["Gasoline", "Diesel", "Hybrid", "Electric"],
        )
        parser.add_argument("transmission", type=str, required=True, choices=["Automatic", "Manual"])
        parser.add_argument("clean_title", type=str, required=True, choices=["Yes", "No"])
        parser.add_argument("meses", type=int, default=12, choices=list(range(1, 61)))

        args = parser.parse_args()

        try:
            # Convert Yes/No to 1/0 for ML model
            clean_title_value = 1 if args["clean_title"] == "Yes" else 0

            data = {
                "model_year": args["model_year"],
                "age": args["age"],
                "fuel_type": args["fuel_type"],
                "transmission": args["transmission"],
                "clean_title": clean_title_value,
            }

            pred_actual = predict_price(data)
            pred_futura = predict_future_price(pred_actual, months_ahead=args["meses"])

            return {
                "datos": {
                    "model_year": args["model_year"],
                    "age": args["age"],
                    "fuel_type": args["fuel_type"],
                    "transmission": args["transmission"],
                    "clean_title": args["clean_title"],
                },
                "meses": args["meses"],
                "precio_actual_estimado": round(pred_actual, 2),
                "precio_estimado_futuro": round(pred_futura, 2),
            }
        except Exception as e:
            api.abort(400, f"Prediction error: {str(e)}")


@ns_vehicles.route("/publish")
class PublishVehicle(Resource):
    @api.doc("publish_vehicle")
    @api.expect(vehicle_listing_model)
    @api.marshal_with(vehicle_listing_response)
    def post(self):
        """Add a new vehicle listing to the platform"""
        try:
            data = api.payload

            # Validate required fields
            required_fields = [
                "model_year",
                "age",
                "fuel_type",
                "transmission",
                "clean_title",
                "precio",
            ]
            if not all(field in data for field in required_fields):
                api.abort(400, f"Missing required fields: {required_fields}")

            # Read existing vehicles
            with open(DB_FILE, "r") as f:
                vehiculos = json.load(f)

            # Generate new ID
            nuevo_id = len(vehiculos) + 1
            data["id"] = nuevo_id

            # Save vehicle
            vehiculos.append(data)
            with open(DB_FILE, "w") as f:
                json.dump(vehiculos, f, indent=4)

            # Convert Yes/No to 1/0 for ML model
            clean_title_value = 1 if data["clean_title"] == "Yes" else 0

            # Calculate recommended price
            pred = predict_price(
                {
                    "model_year": data["model_year"],
                    "age": data["age"],
                    "fuel_type": data["fuel_type"],
                    "transmission": data["transmission"],
                    "clean_title": clean_title_value,
                }
            )

            return {
                "message": "Vehículo publicado con éxito",
                "vehiculo_id": nuevo_id,
                "precio_publicado": data["precio"],
                "precio_recomendado_modelo": round(pred, 2),
                "datos": data,
            }, 201

        except Exception as e:
            api.abort(400, f"Error publishing vehicle: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5004)
