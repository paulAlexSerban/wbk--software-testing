"""Unit tests for the MathUtils class."""

import pytest
from src.utils.math_utils import MathUtils


class TestMathUtils:
    """Unit tests for MathUtils."""

    @pytest.mark.sanity
    @pytest.mark.math
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert MathUtils.add(2, 3) == 5

    @pytest.mark.math
    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        assert MathUtils.add(-1, 1) == 0

    @pytest.mark.sanity
    @pytest.mark.math
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert MathUtils.subtract(5, 3) == 2

    @pytest.mark.math
    def test_subtract_same_numbers(self):
        """Test subtracting same numbers."""
        assert MathUtils.subtract(0, 0) == 0

    @pytest.mark.sanity
    @pytest.mark.math
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert MathUtils.multiply(2, 3) == 6

    @pytest.mark.math
    def test_multiply_negative_and_positive(self):
        """Test multiplying negative and positive numbers."""
        assert MathUtils.multiply(-1, 1) == -1

    @pytest.mark.sanity
    @pytest.mark.math
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert MathUtils.divide(6, 3) == 2

    @pytest.mark.math
    def test_divide_fails(self):
        """Test the divide method for failure cases."""
        with pytest.raises(Exception):
            assert MathUtils.divide(9, 5) == 1.5, "failed test intentionally"

    @pytest.mark.sanity
    @pytest.mark.math
    def test_divide_by_zero_try_except(self):
        """Test division by zero using try-except."""
        try:
            MathUtils.divide(1, 0)
        except ZeroDivisionError:
            assert True
        else:
            assert False

    @pytest.mark.math
    def test_divide_by_zero_pytest_raises(self):
        """Test division by zero using pytest.raises."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
            MathUtils.divide(10, 0)

    @pytest.mark.math
    @pytest.mark.xfail(
        raises=ZeroDivisionError,
        reason="This test is expected to fail due to division by zero.",
    )
    def test_divide_by_zero_pytest_raises_xfail(self):
        """Test division by zero using pytest.raises."""
        assert MathUtils.divide(10, 0)

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (10, 20, 30),
            (-1, 1, 0),
            (0, 0, 0),
            (100, 200, 300),
        ],
    )
    def test_add_with_parametrize(self, a, b, expected):
        """Test add method with parameterized inputs."""
        assert MathUtils.add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (10, 20, 30),
            (-1, 1, 0),
            (0, 0, 0),
            (100, 200, 300),
        ],
        ids=[
            "one_two",
            "ten_twenty",
            "minus_one_plus_one",
            "zero_zero",
            "hundred_two_hundred",
        ],
    )
    def test_add_with_parametrize_ids(self, a, b, expected):
        """Test add method with parameterized inputs and custom IDs."""
        assert MathUtils.add(a, b) == expected

    def test_sum_all(self, numbers_generator):
        """Test sum_all with a valid list."""
        numbers = numbers_generator(500)
        sut = MathUtils.sum_all(numbers)
        expected_sum = sum(numbers)
        print(f"SUT sum of is {sut}, expected {expected_sum}")
        assert sut == expected_sum
