"""Flask application factory and route registration."""

import logging
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from src.controllers.item_controller import ItemController


def create_app(config_name="development"):
    """Create and configure Flask application.

    Args:
        config_name (str): Configuration environment name

    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Load configuration
    app.config.update(
        {
            "DEBUG": config_name == "development",
            "TESTING": config_name == "testing",
            "JSON_SORT_KEYS": False,
        }
    )

    # Register error handlers
    register_error_handlers(app)

    # Register routes
    register_routes(app)

    return app


def register_error_handlers(app: Flask):
    """Register error handlers for the Flask application.

    Args:
        app (Flask): The Flask application instance
    """

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        """Handle HTTP exceptions."""
        app.logger.error(f"HTTP error occurred: {error}")
        return (
            jsonify(
                {
                    "error": error.name,
                    "message": error.description,
                    "status_code": error.code,
                }
            ),
            error.code,
        )

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        """Handle generic exceptions."""
        app.logger.error(f"Unexpected error occurred: {str(error)}")
        return (
            jsonify(
                {
                    "error": "Internal Server Error",
                    "message": "An unexpected error occurred",
                    "status_code": 500,
                }
            ),
            500,
        )


def register_routes(app: Flask):
    """Register routes for the Flask application.

    Args:
        app (Flask): The Flask application instance
    """

    @app.route("/health", methods=["GET"])
    def health():
        """Health check endpoint.

        Returns:
            dict: Health status response
        """
        return jsonify(
            {"status": "ok", "service": "hello-pytest-api", "version": "1.0.0"}
        )

    @app.route("/items", methods=["GET"])
    def get_items():
        """Get all items endpoint.

        Returns:
            Response: JSON response with items list
        """
        try:
            return ItemController.get_items()
        except Exception as e:
            app.logger.error(f"Error fetching items: {str(e)}")
            return jsonify({"error": "Failed to fetch items", "message": str(e)}), 500

    @app.route("/", methods=["GET"])
    def index():
        """Root endpoint.

        Returns:
            dict: Welcome message
        """
        return jsonify(
            {
                "message": "Welcome to Hello PyTest API",
                "endpoints": {"health": "/health", "items": "/items"},
            }
        )


# Create application instance
app = create_app()


if __name__ == "__main__":
    import os

    # Get configuration from environment
    debug_mode = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    port = int(os.getenv("FLASK_PORT", 5000))
    host = os.getenv("FLASK_HOST", "127.0.0.1")

    app.run(debug=debug_mode, port=port, host=host)
