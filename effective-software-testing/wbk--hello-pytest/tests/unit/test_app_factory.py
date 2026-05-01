"""Unit tests for the app factory module."""
from src.app import create_app


class TestAppFactory:
    """Tests for the app factory."""

    def test_create_app_development_config(self, app, teardown_example, request, cmd_opt):
        """Test that the app is created with development config."""
        app = create_app("development")
        assert app.config["DEBUG"] is True
        assert app.config["TESTING"] is False
        print("os_lang: ", request.config.os_lang)  # Example usage of the pytest fixture
        print("cmd_opt: ", cmd_opt.read())  # Example usage of the pytest fixture
        print("custom_config_option: ", request.config.custom_config_option)  # Example usage of the pytest fixture


    def test_create_app_testing_config(self, app, print_request_values):
        """Test that the app is created with testing config."""
        app = create_app("testing")
        assert app.config["TESTING"] is True
        assert app.config["DEBUG"] is False


    def test_create_app_default_config(self, app):
        """Test that the app is created with default config."""
        app = create_app()
        app = create_app()
        assert app.config["JSON_SORT_KEYS"] is False
