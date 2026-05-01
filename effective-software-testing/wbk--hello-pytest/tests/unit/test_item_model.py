import pytest

from src.models.item_model import ItemModel
from tests.utils.util import get_data


class TestItemModel:

    def test_get_all_items_returns_correct_count(self, check_fixture_scope):
        """Test that get_all_items returns the correct number of items."""
        print(id(check_fixture_scope))
        items = ItemModel.get_all_items()
        assert len(items) == 3

    def test_get_all_items_first_item_name(self, check_fixture_scope):
        """Test that the first item has the correct name."""
        items = ItemModel.get_all_items()
        assert items[0]["name"] == "item1"

    def test_get_all_items_second_item_name(self, check_fixture_scope):
        """Test that the second item has the correct name."""
        items = ItemModel.get_all_items()
        assert items[1]["name"] == "item2"

    def test_get_all_items_third_item_name(self, check_fixture_scope):
        """Test that the third item has the correct name."""
        items = ItemModel.get_all_items()
        assert items[2]["name"] == "item3"

    def test_get_item_by_id_existing_item_not_none(self, check_fixture_scope):
        """Test that get_item_by_id returns non-None for existing item."""
        item = ItemModel.get_item_by_id(1)
        assert item is not None

    def test_get_item_by_id_existing_item_correct_name(self, check_fixture_scope):
        """Test that get_item_by_id returns correct name for existing item."""
        item = ItemModel.get_item_by_id(1)
        assert item["name"] == "item1"

    def test_get_item_by_id_non_existing_item_returns_none(self):
        """Test that get_item_by_id returns None for non-existing item."""
        item = ItemModel.get_item_by_id(4)
        assert item is None

    def test_add_item_returns_added_item(self):
        """Test that add_item returns the added item."""
        new_item = {
            "id": 4,
            "name": "item4",
            "description": "This is item 4",
            "vat": 0.02,
            "cost": 25.0,
            "price": 30.0,
        }
        added_item = ItemModel.add_item(new_item)
        assert added_item == new_item

    def test_add_item_increases_total_count(self):
        """Test that add_item increases the total item count."""
        new_item = {
            "id": 5,
            "name": "item5",
            "description": "This is item 5",
            "vat": 0.02,
            "cost": 25.0,
            "price": 30.0,
        }
        initial_count = len(ItemModel.get_all_items())
        ItemModel.add_item(new_item)
        assert len(ItemModel.get_all_items()) == initial_count + 1

    def test_update_item_name_updated(self):
        """Test that update_item updates the item name correctly."""
        updated_item = {
            "name": "updated_item1",
            "description": "Updated description for item 1",
            "cost": 11.0,
            "price": 13.0,
        }
        item = ItemModel.update_item(1, updated_item)
        assert item["name"] == "updated_item1"

    def test_update_item_description_updated(self):
        """Test that update_item updates the item description correctly."""
        updated_item = {
            "name": "updated_item1",
            "description": "Updated description for item 1",
            "cost": 11.0,
            "price": 13.0,
        }
        item = ItemModel.update_item(1, updated_item)
        assert item["description"] == "Updated description for item 1"

    def test_update_item_cost_updated(self):
        """Test that update_item updates the item cost correctly."""
        updated_item = {
            "name": "updated_item1",
            "description": "Updated description for item 1",
            "cost": 11.0,
            "price": 13.0,
        }
        item = ItemModel.update_item(1, updated_item)
        assert item["cost"] == 11.0

    def test_update_item_price_updated(self):
        """Test that update_item updates the item price correctly."""
        updated_item = {
            "name": "updated_item1",
            "description": "Updated description for item 1",
            "cost": 11.0,
            "price": 13.0,
        }
        item = ItemModel.update_item(1, updated_item)
        assert item["price"] == 13.0

    @pytest.mark.parametrize("item_id,name,description,vat,cost,price", get_data())
    def test_add_multiple_items_from_csv(
        self, item_id, name, description, vat, cost, price
    ):
        """Test that multiple items can be added using data from CSV file."""
        item_data = {
            "id": int(item_id),
            "name": name,
            "description": description,
            "vat": float(vat) / 100,  # Convert percentage to decimal (20 -> 0.20)
            "cost": float(cost),
            "price": float(price),
        }

        added_item = ItemModel.add_item(item_data)
        assert added_item == item_data
        assert added_item["id"] == int(item_id)
        assert added_item["name"] == name
        assert added_item["description"] == description
        assert added_item["vat"] == float(vat) / 100
        assert added_item["cost"] == float(cost)
        assert added_item["price"] == float(price)
