#!/usr/bin/python3
"""
This module provides a function to convert a Python object
to its JSON string representation.

The function uses the standard json module to serialize
Python data types into JSON format.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of a Python object.

    This function serializes a Python object to a JSON formatted string
    using the standard json.dumps() method. It does not handle exceptions
    if the object is not serializable.

    Args:
        my_obj: The Python object to be serialized.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
