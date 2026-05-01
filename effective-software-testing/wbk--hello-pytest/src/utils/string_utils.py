"""String utility functions for various string operations."""


def concatenate_strings(*args: str) -> str:
    """Concatenate multiple strings into one."""
    return "".join(args)


def reverse_string(s: str) -> str:
    """Reverse a given string."""
    return s[::-1]


def get_string_length(s: str) -> int:
    """Return the length of a given string."""
    return len(s)


def get_letter_at_index(s: str, index: int) -> str:
    """Return the letter at a given index in the string."""
    return s[index] if 0 <= index < len(s) else ""


def to_uppercase(s: str) -> str:
    """Convert a string to uppercase."""
    return s.upper()


def to_lowercase(s: str) -> str:
    """Convert a string to lowercase."""
    return s.lower()


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def slice_string(text, start, end):
    """Slice a string from start to end.§

    Args:
        text (_type_): _description_
        start (_type_): _description_
        end (_type_): _description_

    Raises:
        IndexError: _description_

    Returns:
        _type_: _description_
    """
    if start >= len(text) and len(text) > 0:
        raise IndexError("Start index out of bounds")
    return text[start:end]


def split_string(s: str, delimiter: str = " ") -> list:
    """Split a string into a list of substrings based on a delimiter."""
    return s.split(delimiter)
