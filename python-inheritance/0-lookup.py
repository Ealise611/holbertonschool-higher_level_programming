#!/usr/bin/python3
"""
This module return a list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Return a list of the available attributes and methods of an object.

    This function takes any Python object and returns a list of all the 
    attribute names and method names that are accessible through the object.
    """
    print(dir(obj))
