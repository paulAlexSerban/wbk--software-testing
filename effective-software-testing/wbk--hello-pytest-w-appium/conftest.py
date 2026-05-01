import pytest
from src.options import get_android_options
from src.drivers import initialize_driver


@pytest.fixture
def setup_driver():
    """Fixture to initialize and clean up the Appium driver."""
    options = get_android_options()
    driver = initialize_driver(options)
    yield driver
    driver.quit()
