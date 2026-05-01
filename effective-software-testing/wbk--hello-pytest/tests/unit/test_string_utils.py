import pytest

from src.utils.string_utils import (
    concatenate_strings,
    reverse_string,
    get_string_length,
    get_letter_at_index,
    to_uppercase,
    to_lowercase,
    is_palindrome,
    slice_string,
    split_string,
)


class TestStringUtils:
    """Unit tests for string utility functions."""

    @pytest.mark.sanity
    @pytest.mark.string
    def test_concatenate_strings_multiple_args(self):
        """Test concatenation of multiple strings."""
        assert concatenate_strings("Hello", " ", "World") == "Hello World"

    @pytest.mark.string
    def test_concatenate_strings_two_args(self):
        """Test concatenation of two strings."""
        assert concatenate_strings("Python", "3") == "Python3"

    @pytest.mark.sanity
    @pytest.mark.string
    def test_reverse_string_normal(self):
        """Test reversing a normal string."""
        assert reverse_string("Hello") == "olleH"

    @pytest.mark.string
    def test_reverse_string_empty(self):
        """Test reversing an empty string."""
        assert reverse_string("") == ""

    @pytest.mark.sanity
    @pytest.mark.string
    def test_get_string_length_normal(self):
        """Test getting the length of a normal string."""
        assert get_string_length("Hello") == 5

    @pytest.mark.string
    def test_get_string_length_empty(self):
        """Test getting the length of an empty string."""
        assert get_string_length("") == 0

    @pytest.mark.sanity
    @pytest.mark.string
    def test_get_letter_at_index_middle(self):
        """Test getting a letter at a middle index."""
        assert get_letter_at_index("Hello", 1) == "e"

    @pytest.mark.string
    def test_get_letter_at_index_last(self):
        """Test getting a letter at the last index."""
        assert get_letter_at_index("Hello", 4) == "o"

    @pytest.mark.string
    def test_get_letter_at_index_out_of_bounds(self):
        """Test getting a letter at an out of bounds index."""
        assert get_letter_at_index("Hello", 5) == ""

    @pytest.mark.sanity
    @pytest.mark.string
    def test_to_uppercase_normal(self):
        """Test converting a lowercase string to uppercase."""
        assert to_uppercase("hello") == "HELLO"

    @pytest.mark.string
    def test_to_uppercase_empty(self):
        """Test converting an empty string to uppercase."""
        assert to_uppercase("") == ""

    @pytest.mark.sanity
    @pytest.mark.string
    def test_to_lowercase_normal(self):
        """Test converting an uppercase string to lowercase."""
        assert to_lowercase("HELLO") == "hello"

    @pytest.mark.string
    def test_to_lowercase_empty(self):
        """Test converting an empty string to lowercase."""
        assert to_lowercase("") == ""

    @pytest.mark.sanity
    @pytest.mark.string
    def test_is_palindrome_true(self):
        """Test checking if a palindrome string returns true."""
        assert is_palindrome("A man a plan a canal Panama")

    @pytest.mark.string
    def test_is_palindrome_false(self):
        """Test checking if a non-palindrome string returns false."""
        assert not is_palindrome("Hello")

    @pytest.mark.sanity
    @pytest.mark.string
    def test_split_string_default_separator(self):
        """Test splitting a string with default separator (space)."""
        assert split_string("Hello World") == ["Hello", "World"]

    @pytest.mark.string
    def test_split_string_custom_separator(self):
        """Test splitting a string with custom separator."""
        assert split_string("Hello,World", ",") == ["Hello", "World"]

    @pytest.mark.string
    def test_split_string_empty(self):
        """Test splitting an empty string."""
        assert split_string("") == [""]

    @pytest.mark.string
    def test_split_string_multiple_parts(self):
        """Test splitting a string into multiple parts."""
        assert split_string("a b c", " ") == ["a", "b", "c"]

    @pytest.mark.sanity
    @pytest.mark.string
    def test_slice_string_beginning(self):
        """Test slicing a string from the beginning."""
        assert slice_string("Hello, World!", 0, 5) == "Hello"

    @pytest.mark.string
    def test_slice_string_middle(self):
        """Test slicing a string from the middle."""
        assert slice_string("Hello, World!", 7, 12) == "World"

    @pytest.mark.string
    def test_slice_string_end_beyond_length(self):
        """Test slicing a string where end index is beyond string length."""
        assert slice_string("Hello", 0, 10) == "Hello"

    @pytest.mark.string
    def test_slice_string_out_of_bounds(self):
        """Test slicing a string with start index out of bounds raises IndexError."""
        with pytest.raises(IndexError):
            slice_string("Hello", 10, 15)