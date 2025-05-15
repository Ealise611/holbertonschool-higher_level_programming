#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles both integers and floats by casting floats to integers.
If invalid types are passed, it raise TypeError.
"""


def add_integer(a, b=98):
    """ Add two integers.
    Casts floats to integer before addition.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
