class MathUtils:
    """Utility class for mathematical operations."""

    @staticmethod
    def add(a: int, b: int) -> int:
        """Return the sum of two integers."""
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        """Return the difference of two integers."""
        return a - b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        """Return the product of two integers."""
        return a * b

    @staticmethod
    def divide(a: int, b: int) -> float:
        """Return the quotient of two integers."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    
    @staticmethod
    def sum_all(numbers: list) -> int:
        """Return the sum of a list of integers."""
        if not all(isinstance(num, int) for num in numbers):
            raise ValueError("All elements must be integers.")
        return sum(numbers)