"""Integration tests for MVC layer router-model binding."""

from unittest.mock import patch
import pytest
from src.models.item_model import ItemModel


class TestMVCRouterModelBinding:
    """Integration tests for MVC router-model binding."""

    # No fixtures needed - app and client come from conftest.py

    @pytest.mark.sanity
    @pytest.mark.router
    def test_items_route_binds_to_model(self, client):
        """Test that /items route properly binds to ItemModel."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = [{"id": 1, "name": "route_test_item"}]

            response = client.get("/items")

            # Verify the route called the model
            mock_get_all.assert_called_once()
            assert response.status_code == 200

            # Verify response data
            data = response.get_json()
            assert data == [{"id": 1, "name": "route_test_item"}]

    @pytest.mark.router
    def test_items_route_handles_model_data_types(self, client):
        """Test that /items route handles different model data types correctly."""
        test_items = [
            {
                "id": 1,
                "name": "item1",
                "description": "Test item 1",
                "vat": 0.05,
                "cost": 10.0,
                "price": 12.0,
                "active": True,
            },
            {
                "id": 2,
                "name": "item2",
                "description": "Test item 2",
                "vat": 0.021,
                "cost": 15.0,
                "price": 18.0,
                "active": False,
            },
        ]

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = test_items

            response = client.get("/items")
            data = response.get_json()

            # Verify data types are preserved through the binding
            assert isinstance(data[0]["id"], int)
            assert isinstance(data[0]["name"], str)
            assert isinstance(data[0]["vat"], float)
            assert isinstance(data[0]["cost"], float)
            assert isinstance(data[0]["price"], float)
            assert isinstance(data[0]["active"], bool)

    @pytest.mark.router
    def test_items_route_handles_empty_model_response(self, client):
        """Test that /items route handles empty model response."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = []

            response = client.get("/items")

            assert response.status_code == 200
            assert response.get_json() == []

    @pytest.mark.router
    def test_items_route_handles_large_model_response(self, client):
        """Test that /items route handles large model response."""
        large_dataset = [
            {"id": i, "name": f"item_{i}", "price": i * 10.0} for i in range(1000)
        ]

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = large_dataset

            response = client.get("/items")
            data = response.get_json()

            assert response.status_code == 200
            assert len(data) == 1000
            assert data[0]["name"] == "item_0"
            assert data[999]["name"] == "item_999"

    @pytest.mark.router
    def test_items_route_model_exception_handling(self, client):
        """Test that /items route properly handles model exceptions."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.side_effect = Exception("Database connection failed")

            response = client.get("/items")

            assert response.status_code == 500
            error_data = response.get_json()
            assert "error" in error_data
            assert "Failed to fetch items" in error_data["error"]

    @pytest.mark.router
    def test_items_route_model_none_response(self, client):
        """Test that /items route handles None response from model."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = None

            response = client.get("/items")

            assert response.status_code == 200
            assert response.get_json() is None

    @pytest.mark.sanity
    @pytest.mark.router
    def test_route_model_binding_preserves_data_structure(self, client):
        """Test that route-model binding preserves complex data structures."""
        complex_items = [
            {
                "id": 1,
                "name": "complex_item",
                "metadata": {
                    "category": "electronics",
                    "tags": ["new", "popular"],
                    "specifications": {
                        "weight": 1.5,
                        "dimensions": {"length": 10, "width": 5, "height": 3},
                    },
                },
                "variants": [
                    {"color": "red", "size": "small", "stock": 10},
                    {"color": "blue", "size": "large", "stock": 5},
                ],
            }
        ]

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = complex_items

            response = client.get("/items")
            data = response.get_json()

            # Verify complex nested structure is preserved
            item = data[0]
            assert item["metadata"]["category"] == "electronics"
            assert item["metadata"]["tags"] == ["new", "popular"]
            assert item["metadata"]["specifications"]["weight"] == 1.5
            assert item["variants"][0]["color"] == "red"
            assert item["variants"][1]["stock"] == 5

    @pytest.mark.router
    def test_route_uses_actual_model_without_mocking(self, client):
        """Test that route actually uses the real model (integration test)."""
        # This test uses the real ItemModel without mocking
        response = client.get("/items")

        assert response.status_code == 200
        data = response.get_json()

        # Verify we get the actual data from item_model.py
        assert isinstance(data, list)
        assert len(data) == 3  # Based on the actual items in item_model.py

        # Verify structure matches the actual model data
        first_item = data[0]
        assert "id" in first_item
        assert "name" in first_item
        assert "description" in first_item
        assert "vat" in first_item
        assert "cost" in first_item
        assert "price" in first_item

    @pytest.mark.router
    def test_route_model_binding_performance(self, client):
        """Test that route-model binding performs within acceptable limits."""
        import time

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = [
                {"id": i, "name": f"item_{i}"} for i in range(100)
            ]

            start_time = time.time()
            response = client.get("/items")
            end_time = time.time()

            assert response.status_code == 200
            assert (end_time - start_time) < 1.0  # Should complete within 1 second

    @pytest.mark.router
    def test_multiple_concurrent_route_model_calls(self, client):
        """Test that concurrent route-model calls work correctly."""
        import concurrent.futures

        def make_request():
            return client.get("/items")

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = [{"id": 1, "name": "concurrent_test"}]

            # Make 10 concurrent requests
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                futures = [executor.submit(make_request) for _ in range(10)]
                responses = [future.result() for future in futures]

            # Verify all requests succeeded
            for response in responses:
                assert response.status_code == 200
                assert response.get_json() == [{"id": 1, "name": "concurrent_test"}]

            # Verify model was called for each request
            assert mock_get_all.call_count == 10

    @pytest.mark.router
    def test_route_model_binding_with_app_context(self, client):
        """Test route-model binding within Flask application context."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = [{"id": 1, "name": "context_test"}]

            response = client.get("/items")

            assert response.status_code == 200
            assert response.get_json() == [{"id": 1, "name": "context_test"}]

    @pytest.mark.router
    def test_health_route_independence_from_model(self, client):
        """Test that health route works independently from model."""
        # Health route should work even if ItemModel fails
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.side_effect = Exception("Model is broken")

            response = client.get("/health")

            assert response.status_code == 200
            data = response.get_json()
            assert data["status"] == "ok"
            assert data["service"] == "hello-pytest-api"
            # Health route should not call ItemModel
            mock_get_all.assert_not_called()

    @pytest.mark.router
    def test_index_route_independence_from_model(self, client):
        """Test that index route works independently from model."""
        # Index route should work even if ItemModel fails
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.side_effect = Exception("Model is broken")

            response = client.get("/")

            assert response.status_code == 200
            data = response.get_json()
            assert "Welcome to Hello PyTest API" in data["message"]
            assert "endpoints" in data
            # Index route should not call ItemModel
            mock_get_all.assert_not_called()
