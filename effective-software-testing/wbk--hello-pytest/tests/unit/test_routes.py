import pytest
from src.app import create_app


class TestRoutes:
    # No fixture needed - client comes from conftest.py

    def test_health_endpoint(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "ok"
        assert data["service"] == "hello-pytest-api"

    def test_index_endpoint(self, client):
        response = client.get("/")
        assert response.status_code == 200
        data = response.get_json()
        assert "Welcome to Hello PyTest API" in data["message"]
        assert "endpoints" in data
