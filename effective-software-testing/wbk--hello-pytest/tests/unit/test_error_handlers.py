import pytest
from werkzeug.exceptions import NotFound
from src.app import create_app


class TestErrorHandlers:
    @pytest.fixture
    def client(self):
        app = create_app("testing")

        # Add test route that raises exceptions
        @app.route("/test-404")
        def test_404():
            raise NotFound("Test not found")

        @app.route("/test-500")
        def test_500():
            raise Exception("Test generic error")

        return app.test_client()

    def test_http_exception_handler(self, client):
        response = client.get("/test-404")
        assert response.status_code == 404
        data = response.get_json()
        assert data["error"] == "Not Found"
        assert data["status_code"] == 404

    def test_generic_exception_handler(self, client):
        response = client.get("/test-500")
        assert response.status_code == 500
        data = response.get_json()
        assert data["error"] == "Internal Server Error"
        assert data["status_code"] == 500
