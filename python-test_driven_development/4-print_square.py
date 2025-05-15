#!/usr/bin/python3
"""
This module defines a function that prints a square made of '#' characters.

The size of the square must be a non-negative integer.
"""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If size is not an integer or is a float.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(2)
        ##
        ##
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print('#' * size)
