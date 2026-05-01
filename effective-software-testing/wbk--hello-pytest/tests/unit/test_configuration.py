import pytest
import os
from unittest.mock import patch
from src.app import create_app


class TestConfiguration:
    def test_environment_variables_loading(self):
        with patch.dict(
            os.environ,
            {"FLASK_DEBUG": "False", "FLASK_PORT": "8080", "FLASK_HOST": "0.0.0.0"},
        ):
            # Test that environment variables are read correctly
            from src.app import app  # This will use env vars

            # Add assertions based on your app configuration

    @pytest.mark.parametrize(
        "config_name,expected_debug,expected_testing",
        [
            ("development", True, False),
            ("testing", False, True),
            ("production", False, False),
        ],
    )
    def test_different_configurations(
        self, config_name, expected_debug, expected_testing
    ):
        app = create_app(config_name)
        assert app.config["DEBUG"] == expected_debug
        assert app.config["TESTING"] == expected_testing
