#!/usr/bin/python3
"""
this module has two function
1-serialize_and_save_to_file
2-load_and_deserialize
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    this function serialize and save data to file
    """
    with open(filename, 'w') as f:
        return json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, 'r') as f:
        return json.load(f)
