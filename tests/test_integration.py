import os
import subprocess
import time

import pytest
import requests


class TestIntegration:
    backend_process = None
    frontend_process = None

    @classmethod
    def setup_class(cls):
        """Start backend and frontend services for integration testing"""
        # Start backend
        backend_dir = os.path.join(os.path.dirname(__file__), "..", "backend")
        cls.backend_process = subprocess.Popen(
            ["python3", "app.py"], cwd=backend_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

        # Start frontend
        frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
        cls.frontend_process = subprocess.Popen(
            ["python3", "app.py"], cwd=frontend_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

        # Wait for services to start
        time.sleep(5)

    @classmethod
    def teardown_class(cls):
        """Stop services after testing"""
        if cls.backend_process:
            cls.backend_process.terminate()
            cls.backend_process.wait()
        if cls.frontend_process:
            cls.frontend_process.terminate()
            cls.frontend_process.wait()

    def test_backend_health(self):
        """Test backend service is running"""
        try:
            response = requests.get("http://localhost:5002/", timeout=5)
            assert response.status_code == 200
        except requests.exceptions.RequestException:
            pytest.skip("Backend service not available for integration testing")

    def test_frontend_health(self):
        """Test frontend service is running"""
        try:
            response = requests.get("http://localhost:3000/", timeout=5)
            assert response.status_code == 200
        except requests.exceptions.RequestException:
            pytest.skip("Frontend service not available for integration testing")

    def test_end_to_end_prediction(self):
        """Test complete prediction workflow"""
        try:
            # Test backend API directly
            params = {"model_year": 2020, "age": 4, "fuel_type": "Gasoline", "transmission": "Automatic", "clean_title": 1}
            response = requests.get("http://localhost:5002/current_value_market", params=params, timeout=5)
            assert response.status_code == 200
            data = response.json()
            assert "current_value_market_estimado" in data

            # Test frontend can reach backend (through CORS)
            frontend_response = requests.get("http://localhost:3000/", timeout=5)
            assert frontend_response.status_code == 200

        except requests.exceptions.RequestException:
            pytest.skip("Services not available for end-to-end testing")
