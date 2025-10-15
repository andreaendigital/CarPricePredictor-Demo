import pytest
import sys
import os
import tempfile
import shutil

# Add backend to path and set up environment
backend_dir = os.path.join(os.path.dirname(__file__), "..", "backend")
sys.path.append(backend_dir)

# Create temporary file for testing to avoid modifying the real vehiculos.json
temp_db = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
original_db = os.path.join(backend_dir, "vehiculos.json")
if os.path.exists(original_db):
    shutil.copy2(original_db, temp_db.name)
else:
    temp_db.write("[]")
temp_db.close()

# Set environment variables before importing app
os.environ["MODEL_PATH"] = os.path.join(backend_dir, "modelo", "modelo.joblib")
os.environ["DB_PATH"] = temp_db.name

# Change to backend directory for relative paths
original_cwd = os.getcwd()
os.chdir(backend_dir)

try:
    from app import app
finally:
    os.chdir(original_cwd)


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test the home endpoint returns correct response"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data is not None
    assert "message" in data
    assert "endpoints" in data


def test_precio_actual_endpoint(client):
    """Test current price prediction endpoint"""
    response = client.get("/precio_actual?model_year=2020&age=4&fuel_type=Gasoline&transmission=Automatic&clean_title=1")
    assert response.status_code == 200
    data = response.get_json()
    assert "precio_actual_estimado" in data
    assert "datos" in data


def test_precio_actual_missing_params(client):
    """Test current price endpoint with missing parameters"""
    response = client.get("/precio_actual?model_year=2020")
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


def test_prediccion_futura_endpoint(client):
    """Test future price prediction endpoint"""
    response = client.get(
        "/prediccion_futura?model_year=2020&age=4&fuel_type=Gasoline&transmission=Automatic&clean_title=1&meses=12"
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "precio_actual_estimado" in data
    assert "precio_estimado_futuro" in data
    assert "meses" in data


def test_publicar_vehiculo_endpoint(client):
    """Test vehicle publishing endpoint"""
    vehicle_data = {
        "model_year": 2020,
        "age": 4,
        "fuel_type": "Gasoline",
        "transmission": "Automatic",
        "clean_title": 1,
        "precio": 25000000,
    }
    response = client.post("/publicar_vehiculo", json=vehicle_data)
    assert response.status_code == 201
    data = response.get_json()
    assert "vehiculo_id" in data
    assert "precio_recomendado_modelo" in data


def teardown_module():
    """Clean up temporary file after tests"""
    temp_file = os.environ.get("DB_PATH")
    if temp_file and os.path.exists(temp_file):
        os.unlink(temp_file)
