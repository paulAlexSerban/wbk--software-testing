"""Integration tests for MVC layer controller behavior."""

from unittest.mock import patch

import pytest
from flask import json

from src.controllers.item_controller import ItemController
from src.models.item_model import ItemModel


class TestItemControllerIntegration:
    """Integration tests for ItemController MVC layer behavior."""

    # No fixtures needed - app and client come from conftest.py

    @pytest.mark.sanity
    @pytest.mark.controller
    def test_get_items_returns_json_response(self, app):
        """Test that get_items returns a proper JSON response."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = [
                {"id": 1, "name": "test_item1"},
                {"id": 2, "name": "test_item2"},
            ]

            response = ItemController.get_items()

            assert response.status_code == 200
            assert response.content_type == "application/json"

    @pytest.mark.controller
    def test_get_items_calls_model_method(self, app):
        """Test that get_items properly calls the model method."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = []

            ItemController.get_items()

            mock_get_all.assert_called_once()

    @pytest.mark.sanity
    @pytest.mark.controller
    def test_get_items_returns_expected_data_structure(self, app):
        """Test that get_items returns the expected data structure."""
        test_items = [{"id": 1, "name": "item1"}, {"id": 2, "name": "item2"}]

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = test_items

            response = ItemController.get_items()
            response_data = json.loads(response.data.decode("utf-8"))

            assert isinstance(response_data, list)
            assert len(response_data) == 2
            assert response_data == test_items

    @pytest.mark.controller
    def test_get_items_handles_empty_list(self, app):
        """Test that get_items properly handles empty item list."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = []

            response = ItemController.get_items()
            response_data = json.loads(response.data.decode("utf-8"))

            assert response.status_code == 200
            assert isinstance(response_data, list)
            assert len(response_data) == 0

    @pytest.mark.controller
    def test_get_items_handles_single_item(self, app):
        """Test that get_items properly handles single item."""
        test_item = [{"id": 1, "name": "single_item"}]

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = test_item

            response = ItemController.get_items()
            response_data = json.loads(response.data.decode("utf-8"))

            assert response.status_code == 200
            assert len(response_data) == 1
            assert response_data[0]["name"] == "single_item"

    @pytest.mark.controller
    def test_get_items_handles_large_dataset(self, app):
        """Test that get_items properly handles large dataset."""
        large_dataset = [{"id": i, "name": f"item_{i}"} for i in range(1000)]

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = large_dataset

            response = ItemController.get_items()
            response_data = json.loads(response.data.decode("utf-8"))

            assert response.status_code == 200
            assert len(response_data) == 1000
            assert response_data[0]["name"] == "item_0"
            assert response_data[999]["name"] == "item_999"

    @pytest.mark.controller
    def test_get_items_preserves_data_integrity(self, app):
        """Test that get_items preserves data integrity from model to response."""
        test_items = [
            {"id": 1, "name": "item1", "description": "Test item 1", "price": 10.99},
            {"id": 2, "name": "item2", "description": "Test item 2", "price": 20.50},
        ]

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = test_items

            response = ItemController.get_items()
            response_data = json.loads(response.data.decode("utf-8"))

            # Verify all fields are preserved
            assert response_data[0]["id"] == 1
            assert response_data[0]["name"] == "item1"
            assert response_data[0]["description"] == "Test item 1"
            assert response_data[0]["price"] == 10.99

            assert response_data[1]["id"] == 2
            assert response_data[1]["name"] == "item2"
            assert response_data[1]["description"] == "Test item 2"
            assert response_data[1]["price"] == 20.50

    @pytest.mark.controller
    def test_get_items_model_exception_propagation(self, app):
        """Test that controller properly handles model exceptions."""
        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.side_effect = Exception("Database connection failed")

            with pytest.raises(Exception, match="Database connection failed"):
                ItemController.get_items()

    @pytest.mark.controller
    def test_controller_model_interaction_flow(self, app):
        """Test the complete MVC flow from controller to model and back."""
        expected_items = [{"id": 1, "name": "integration_test_item"}]

        with patch.object(ItemModel, "get_all_items") as mock_get_all:
            mock_get_all.return_value = expected_items

            # Call controller method
            response = ItemController.get_items()

            # Verify model was called
            mock_get_all.assert_called_once()

            # Verify response properties
            assert response.status_code == 200
            assert response.content_type == "application/json"

            # Verify response data
            response_data = json.loads(response.data.decode("utf-8"))
            assert response_data == expected_items
