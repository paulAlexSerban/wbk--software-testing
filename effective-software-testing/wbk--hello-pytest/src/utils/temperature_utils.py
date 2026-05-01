def centigrade_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_centigrade(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def kelvin_to_centigrade(kelvin: float) -> float:
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def centigrade_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return celsius + 273.15
