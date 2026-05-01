items = [
    {
        "id": 1,
        "name": "item1",
        "description": "This is item 1",
        "vat": 0.05,
        "cost": 10.0,
        "price": 12.0,
    },
    {
        "id": 2,
        "name": "item2",
        "description": "This is item 2",
        "vat": 0.021,
        "cost": 15.0,
        "price": 18.0,
    },
    {
        "id": 3,
        "name": "item3",
        "description": "This is item 3",
        "vat": 0.015,
        "cost": 20.0,
        "price": 23.0,
    },
]


class ItemModel:
    @staticmethod
    def get_all_items():
        return items
    
    @staticmethod
    def get_item_by_id(item_id):
        for item in items:
            if item["id"] == item_id:
                return item
        return None
    
    @staticmethod
    def add_item(item):
        if not isinstance(item, dict):
            raise ValueError("Item must be a dictionary.")
        if "id" not in item or "name" not in item or "description" not in item:
            raise ValueError("Item must have id, name, and description.")
        items.append(item)
        return item
    
    @staticmethod
    def update_item(item_id, updated_item):
        for index, item in enumerate(items):
            if item["id"] == item_id:
                items[index].update(updated_item)
                return items[index]
        raise ValueError("Item not found.")
    