#!/usr/bin/python3
"""
This module provides a utility function to check if an object is an instance
of a specified class or an instance of a subclass that inherits from it.

It can be used to confirm type relationships that include inheritance chains.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or its subclass.

    This function returns True if the object is an instance of the specified
    class or any class derived from it. It supports inheritance checks.
    """
    return isinstance(obj, a_class)
