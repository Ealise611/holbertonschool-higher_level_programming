#!/usr/bin/python3
"""
This module has func that writes an obj to a text file
using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    this func writes an obj to a text file using JSON rep
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
