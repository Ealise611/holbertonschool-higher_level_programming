#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly an instance
of a specified class.

It does not consider inheritance — only direct instances of the class will return True.
"""


def is_same_class(obj, a_class):
    """
    Determine if an object is exactly an instance of the specified class.

    This function returns True only if the object is an instance of the class
    provided as the second argument. It does not consider subclasses.
    """
    return (type(obj) is a_class)
