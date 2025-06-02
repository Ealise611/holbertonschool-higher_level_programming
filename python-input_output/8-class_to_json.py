#!/usr/bin/python3
"""
this module has func return the dictionary description
with simple data structure for JSON serialisation of
an object
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description with simple
    data structure for JSON
    """
    return obj.__dict__
