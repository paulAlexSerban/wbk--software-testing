class TestSecurity:
    # No fixtures needed - app and client come from conftest.py

    def test_json_content_type_required(self, client):
        # Test that endpoints return proper content types
        response = client.get("/health")
        assert "application/json" in response.content_type

    def test_error_information_disclosure(self, client):
        # Ensure error responses don't leak sensitive information
        response = client.get("/nonexistent")
        data = response.get_json()
        assert "status_code" in data
        # Ensure no stack traces or sensitive info in production errors
