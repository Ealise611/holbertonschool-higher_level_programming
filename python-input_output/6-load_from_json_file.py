#!/usr/bin/python3
"""
This module has func that create an obj from a JSON file

"""

import json


def load_from_json_file(filename):
    """
    this func creates an obj from a Json file
    """
    with open(filename, 'r') as f:
        return json.load(f)
