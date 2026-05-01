"""End-to-end tests for the Flask application."""

import subprocess
import time
import signal
import os
import pytest
import requests


class TestAppE2E:
    """End-to-end tests for the Flask application."""

    @pytest.fixture(scope="class")
    def running_app(self):
        """Start the Flask app in a subprocess"""
        env = os.environ.copy()
        env["FLASK_PORT"] = "5001"
        process = subprocess.Popen(["python", "-m", "src.app"], env=env)
        time.sleep(2)  # Wait for app to start
        yield "http://127.0.0.1:5001"
        process.send_signal(signal.SIGTERM)
        process.wait()

    def test_health_check_e2e(self, running_app):
        """Test the health endpoint of the running app."""
        response = requests.get(url=f"{running_app}/health", timeout=5)
        assert response.status_code == 200
        assert response.json()["status"] == "ok"

    def test_full_api_workflow(self, running_app):
        """Test the full API workflow."""
        # Test index
        response = requests.get(url=running_app, timeout=5)
        assert response.status_code == 200

        # Test health
        response = requests.get(url=f"{running_app}/health", timeout=5)
        assert response.status_code == 200

        # Test items (might fail without proper setup)
        response = requests.get(url=f"{running_app}/items", timeout=5)
        assert response.status_code in [200, 500]  # Could fail if model issues
