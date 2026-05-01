from flask import jsonify

from src.models.item_model import ItemModel


class ItemController:
    @staticmethod
    def get_items():
        return jsonify(ItemModel.get_all_items())
