import os
from unittest.mock import patch
from random import randint
import pytest
from src.app import create_app


# conftest.py fixtures are automatically available to all test files
@pytest.fixture(scope="session")
def app():
    """Create application for the tests."""
    app = create_app("testing")
    return app


@pytest.fixture(scope="function")
def client(app):
    """Create a test client."""
    return app.test_client()

@pytest.fixture(scope="class", autouse=True)
def check_fixture_scope():
    """Check the fixture scope."""
    yield print("on yield - check_fixture_scope fixture")
    print("\nCheck fixture scope completed.")

@pytest.fixture
def mock_item_controller():
    """Mock ItemController for testing."""
    with patch("src.controllers.item_controller.ItemController") as mock:
        yield mock


@pytest.fixture(scope="function")
def teardown_example():
    """Example fixture for teardown."""
    yield print("on yield - teardown_example fixture")
    print("after yield - teardown_example fixture completed")


@pytest.fixture(scope="function")
def print_request_values(request):
    """Print the test value from the request."""
    print("\nin Fixture print_request_values - test_value")
    print(f"\nFixture scope: {request.scope}")
    print(f"\nCalling function: {request.function.__name__}")


@pytest.fixture
def numbers_generator():
    """Example fixture to demonstrate factory pattern."""

    generated_numbers = []

    def generate_numbers(n):
        """Generate a list of n random numbers."""

        numbers = [randint(1, 100) for _ in range(n)]
        generated_numbers.extend(numbers)
        return numbers

    yield generate_numbers
    print("\nGenerated numbers:", generated_numbers)


def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--envconfig",
        default="QA",
        action="store",
        help="Environment configuration file to use (QA or PROD).",
        dest="env_configuration",
        choices=["QA", "PROD"],
        required=True,
    )
    parser.addoption(
        "--custom_config_option",
        action="store",
        default="default_config_value",
    )


def pytest_configure(config):
    """Configure pytest settings."""
    config.os_lang = os.environ.get("LANG")
    config.custom_config_option = config.getoption("custom_config_option")


QA_CONFIG = os.path.join(os.path.dirname(__file__), "qa.prop")
PROD_CONFIG = os.path.join(os.path.dirname(__file__), "prod.prop")


@pytest.fixture()
def cmd_opt(pytestconfig):
    """Get command line option value."""
    print("In CmdOpt fixture function")
    opt = pytestconfig.getoption("env_configuration")
    if opt == "PROD":
        file = open(file=PROD_CONFIG, mode="r", encoding="utf-8")
    else:
        file = open(file=QA_CONFIG, mode="r", encoding="utf-8")
    yield file
