"""Unit tests for temperature conversion utilities."""

import sys
import pytest

from src.utils.temperature_utils import (
    centigrade_to_fahrenheit,
    fahrenheit_to_centigrade,
    kelvin_to_centigrade,
    centigrade_to_kelvin,
)


class TestTemperatureUtils:
    """Unit tests for temperature conversion utilities."""

    @pytest.mark.sanity
    def test_centigrade_to_fahrenheit_freezing(self):
        """Test Celsius to Fahrenheit conversion for freezing point."""
        assert centigrade_to_fahrenheit(0) == 32

    def test_centigrade_to_fahrenheit_boiling(self):
        """Test Celsius to Fahrenheit conversion for boiling point."""
        assert centigrade_to_fahrenheit(100) == 212

    @pytest.mark.sanity
    def test_fahrenheit_to_centigrade_freezing(self):
        """Test Fahrenheit to Celsius conversion for freezing point."""
        assert fahrenheit_to_centigrade(32) == 0

    def test_fahrenheit_to_centigrade_boiling(self):
        """Test Fahrenheit to Celsius conversion for boiling point."""
        assert fahrenheit_to_centigrade(212) == 100

    @pytest.mark.sanity
    def test_kelvin_to_centigrade_absolute_zero(self):
        """Test Kelvin to Celsius conversion for absolute zero."""
        assert kelvin_to_centigrade(273.15) == 0

    def test_kelvin_to_centigrade_boiling(self):
        """Test Kelvin to Celsius conversion for water boiling point."""
        assert kelvin_to_centigrade(373.15) == 100

    @pytest.mark.sanity
    def test_centigrade_to_kelvin_freezing(self):
        """Test Celsius to Kelvin conversion for water freezing point."""
        assert centigrade_to_kelvin(0) == 273.15

    def test_centigrade_to_kelvin_boiling(self):
        """Test Celsius to Kelvin conversion for water boiling point."""
        assert centigrade_to_kelvin(100) == 373.15

    @pytest.mark.skip(reason="Skipping this test for demonstration purposes")
    def test_centigrade_to_fahrenheit_skip_demo_freezing(self):
        """Test Celsius to Fahrenheit conversion - skipped demo."""
        assert centigrade_to_fahrenheit(0) == 32

    @pytest.mark.skip(reason="Skipping this test for demonstration purposes")
    def test_centigrade_to_fahrenheit_skip_demo_boiling(self):
        """Test Celsius to Fahrenheit conversion - skipped demo."""
        assert centigrade_to_fahrenheit(100) == 212

    @pytest.mark.skipif(
        condition=sys.version_info < (3, 13), reason="Requires Python 3.13 or higher"
    )
    def test_centigrade_to_fahrenheit_python313_freezing(self):
        """Test Celsius to Fahrenheit conversion - Python 3.13+ only."""
        assert centigrade_to_fahrenheit(0) == 32

    @pytest.mark.skipif(
        condition=sys.version_info < (3, 13), reason="Requires Python 3.13 or higher"
    )
    def test_centigrade_to_fahrenheit_python313_boiling(self):
        """Test Celsius to Fahrenheit conversion - Python 3.13+ only."""
        assert centigrade_to_fahrenheit(100) == 212