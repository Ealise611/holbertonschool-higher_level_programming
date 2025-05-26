#!/usr/bin/python3
"""
This module provides a function to determine whether an object is an instance
of a subclass (direct or indirect) of a specified class.

It does not return True for objects that are instances of the
specified class itself,
only for those that inherit from it.
"""


def inherits_from(obj, a_class):
    """
    Determine if an object is an instance of a subclass of the specified class.

    This function returns True if the object's class is a subclass
    (either directly
    or indirectly) of the specified class. It returns False if the object is
    an instance of the specified class itself or of an unrelated class.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
