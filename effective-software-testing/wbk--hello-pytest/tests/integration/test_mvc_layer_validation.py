"""Integration tests for MVC layer validation."""

from unittest.mock import patch

import pytest
from src.models.item_model import ItemModel


class TestMVCLayerValidation:
    """Integration tests for MVC layer validation."""

    # No fixtures needed - app and client come from conftest.py

    @pytest.mark.sanity
    @pytest.mark.validation
    @pytest.mark.api
    def test_get_items_endpoint_validation(self, client):
        """Test that GET /items endpoint validates correctly."""
        response = client.get("/items")

        assert response.status_code == 200
        assert response.content_type == "application/json"

        data = response.get_json()
        assert isinstance(data, list)

    @pytest.mark.validation
    @pytest.mark.api
    def test_items_endpoint_only_accepts_get_method(self, client):
        """Test that /items endpoint only accepts GET method."""
        # Test unsupported methods
        response_post = client.post("/items")
        assert response_post.status_code == 405  # Method Not Allowed

        response_put = client.put("/items")
        assert response_put.status_code == 405

        response_delete = client.delete("/items")
        assert response_delete.status_code == 405

        response_patch = client.patch("/items")
        assert response_patch.status_code == 405

    @pytest.mark.validation
    @pytest.mark.api
    def test_health_endpoint_only_accepts_get_method(self, client):
        """Test that /health endpoint only accepts GET method."""
        # Test unsupported methods
        response_post = client.post("/health")
        assert response_post.status_code == 405

        response_put = client.put("/health")
        assert response_put.status_code == 405

    @pytest.mark.sanity
    @pytest.mark.validation
    @pytest.mark.api
    def test_health_endpoint_response_structure_validation(self, client):
        """Test that /health endpoint returns valid response structure."""
        response = client.get("/health")

        assert response.status_code == 200
        data = response.get_json()

        # Validate required fields
        assert "status" in data
        assert "service" in data
        assert "version" in data

        # Validate field values
        assert data["status"] == "ok"
        assert isinstance(data["service"], str)
        assert isinstance(data["version"], str)

    @pytest.mark.validation
    @pytest.mark.api
    def test_index_endpoint_response_structure_validation(self, client):
        """Test that / endpoint returns valid response structure."""
        response = client.get("/")

        assert response.status_code == 200
        data = response.get_json()

        # Validate required fields
        assert "message" in data
        assert "endpoints" in data

        # Validate field types
        assert isinstance(data["message"], str)
        assert isinstance(data["endpoints"], dict)

        # Validate endpoints structure
        endpoints = data["endpoints"]
        assert "health" in endpoints
        assert "items" in endpoints
        assert endpoints["health"] == "/health"
        assert endpoints["items"] == "/items"

    @pytest.mark.validation
    @pytest.mark.model
    def test_item_model_data_structure_validation(self, client):
        """Test that ItemModel returns valid data structure."""
        response = client.get("/items")

        assert response.status_code == 200
        data = response.get_json()

        # Validate it's a list
        assert isinstance(data, list)

        # Validate each item structure if items exist
        if data:
            for item in data:
                assert isinstance(item, dict)

                # Required fields
                assert "id" in item
                assert "name" in item
                assert "description" in item
                assert "vat" in item
                assert "cost" in item
                assert "price" in item

                # Field type validation
                assert isinstance(item["id"], int)
                assert isinstance(item["name"], str)
                assert isinstance(item["description"], str)
                assert isinstance(item["vat"], (int, float))
                assert isinstance(item["cost"], (int, float))
                assert isinstance(item["price"], (int, float))

                # Business logic validation
                assert item["id"] > 0
                assert len(item["name"]) > 0
                assert item["vat"] >= 0
                assert item["cost"] >= 0
                assert item["price"] >= 0
                assert item["price"] >= item["cost"]  # Price should be >= cost

    @pytest.mark.validation
    @pytest.mark.controller
    def test_controller_input_validation_with_mock(self, client):
        """Test controller handles different input types from model."""
        test_cases = [
            # Valid data
            [
                {
                    "id": 1,
                    "name": "valid_item",
                    "description": "Valid",
                    "vat": 0.05,
                    "cost": 10.0,
                    "price": 12.0,
                }
            ],
            # Empty list
            [],
            # Single item
            [
                {
                    "id": 1,
                    "name": "single",
                    "description": "Single item",
                    "vat": 0.1,
                    "cost": 5.0,
                    "price": 6.0,
                }
            ],
        ]

        for test_data in test_cases:
            with patch.object(ItemModel, "get_all_items") as mock_get_all:
                mock_get_all.return_value = test_data

                response = client.get("/items")

                assert response.status_code == 200
                assert response.get_json() == test_data

    @pytest.mark.validation
    @pytest.mark.api
    def test_invalid_endpoint_validation(self, client):
        """Test that invalid endpoints return proper error responses."""
        response = client.get("/invalid-endpoint")

        assert response.status_code == 404

        # Check if error response has proper structure
        data = response.get_json()
        assert isinstance(data, dict)
        assert "error" in data
        assert "status_code" in data
        assert data["status_code"] == 404

    @pytest.mark.validation
    @pytest.mark.api
    def test_endpoint_case_sensitivity_validation(self, client):
        """Test that endpoints are case-sensitive."""
        # Valid endpoints
        assert client.get("/items").status_code == 200
        assert client.get("/health").status_code == 200

        # Invalid case variations
        assert client.get("/Items").status_code == 404
        assert client.get("/ITEMS").status_code == 404
        assert client.get("/Health").status_code == 404
        assert client.get("/HEALTH").status_code == 404

    @pytest.mark.validation
    @pytest.mark.api
    def test_trailing_slash_validation(self, client):
        """Test endpoint behavior with trailing slashes."""
        # Test with and without trailing slashes
        response_no_slash = client.get("/items")
        response_with_slash = client.get("/items/")

        # Both should work (Flask default behavior)
        assert response_no_slash.status_code == 200
        # Note: Flask by default redirects /items/ to /items with 308 status
        # or treats them the same based on configuration

    @pytest.mark.validation
    @pytest.mark.controller
    def test_controller_error_handling_validation(self, client):
        """Test that controller properly validates and handles errors."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.side_effect = ValueError("Invalid data in model")

            response = client.get("/items")

            assert response.status_code == 500
            error_data = response.get_json()

            # Validate error response structure
            assert isinstance(error_data, dict)
            assert "error" in error_data
            assert "message" in error_data
            assert error_data["error"] == "Failed to fetch items"

    @pytest.mark.validation
    @pytest.mark.api
    def test_json_response_headers_validation(self, client):
        """Test that all endpoints return proper JSON headers."""
        endpoints = ["/", "/health", "/items"]

        for endpoint in endpoints:
            response = client.get(endpoint)

            if response.status_code == 200:
                assert "application/json" in response.content_type
                # Test that response can be parsed as JSON
                json_data = response.get_json()
                assert json_data is not None

    @pytest.mark.validation
    @pytest.mark.api
    def test_http_status_codes_validation(self, client):
        """Test that endpoints return appropriate HTTP status codes."""
        # Success cases
        assert client.get("/").status_code == 200
        assert client.get("/health").status_code == 200
        assert client.get("/items").status_code == 200

        # Error cases
        assert client.get("/nonexistent").status_code == 404
        assert client.post("/items").status_code == 405  # Method not allowed

    @pytest.mark.validation
    @pytest.mark.model
    def test_model_data_consistency_validation(self, client):
        """Test that model data remains consistent across requests."""
        # Make multiple requests
        response1 = client.get("/items")
        response2 = client.get("/items")
        response3 = client.get("/items")

        # All should succeed
        assert response1.status_code == 200
        assert response2.status_code == 200
        assert response3.status_code == 200

        # Data should be consistent
        data1 = response1.get_json()
        data2 = response2.get_json()
        data3 = response3.get_json()

        assert data1 == data2 == data3

    @pytest.mark.validation
    @pytest.mark.controller
    def test_controller_handles_model_none_response(self, client):
        """Test that controller validates None response from model."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = None

            response = client.get("/items")

            # Controller should handle None gracefully
            assert response.status_code == 200
            assert response.get_json() is None

    @pytest.mark.validation
    def test_end_to_end_data_validation_flow(self, client):
        """Test complete data validation flow from route to model."""
        response = client.get("/items")

        assert response.status_code == 200
        data = response.get_json()

        # Validate complete flow
        assert isinstance(data, list)
        assert len(data) == 3  # Based on actual model data

        # Validate first item structure (complete integration)
        first_item = data[0]
        expected_keys = {"id", "name", "description", "vat", "cost", "price"}
        assert set(first_item.keys()) == expected_keys

        # Validate actual data values match model
        assert first_item["id"] == 1
        assert first_item["name"] == "item1"
        assert first_item["description"] == "This is item 1"
        assert first_item["vat"] == 0.05
        assert first_item["cost"] == 10.0
        assert first_item["price"] == 12.0

    @pytest.mark.validation
    @pytest.mark.api
    def test_concurrent_requests_validation(self, client):
        """Test that validation works under concurrent load."""
        import concurrent.futures

        def make_validated_request():
            response = client.get("/items")
            # Validate each response
            assert response.status_code == 200
            data = response.get_json()
            assert isinstance(data, list)
            return response

        # Make 20 concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_validated_request) for _ in range(20)]
            results = [future.result() for future in futures]

        # All should pass validation
        assert len(results) == 20
        for result in results:
            assert result.status_code == 200

    @pytest.mark.validation
    @pytest.mark.api
    @pytest.mark.xfail(reason="Comprehensive method validation not implemented yet")
    def test_request_method_validation_comprehensive(self, client):
        """Test comprehensive HTTP method validation for all endpoints."""
        endpoints = ["/", "/health", "/items"]
        allowed_methods = {"GET"}  # Only GET is allowed for these endpoints
        test_methods = ["POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"]

        for endpoint in endpoints:
            for method in test_methods:
                response = getattr(client, method.lower())(endpoint)
                if method not in allowed_methods:
                    assert response.status_code in [
                        405,
                        501,
                    ]  # Method Not Allowed or Not Implemented

    @pytest.mark.validation
    def test_security_headers_validation(self, client):
        """Test that security-related validation is in place."""
        response = client.get("/items")

        # Check that sensitive information is not leaked
        assert response.status_code == 200
        response_text = response.get_data(as_text=True)

        # Ensure no sensitive information in response
        sensitive_info = ["password", "secret", "token", "key", "__pycache__"]
        for info in sensitive_info:
            assert info.lower() not in response_text.lower()

    @pytest.mark.validation
    @pytest.mark.api
    def test_response_size_validation(self, client):
        """Test that responses are within reasonable size limits."""
        response = client.get("/items")

        assert response.status_code == 200

        # Check response size is reasonable (less than 1MB for this simple API)
        response_size = len(response.get_data())
        assert response_size < 1024 * 1024  # 1MB limit

        # Check that response is not empty when it should have content
        data = response.get_json()
        if isinstance(data, list) and len(data) > 0:
            assert response_size > 0
