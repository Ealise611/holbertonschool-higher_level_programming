#!/usr/bin/python3
"""
This module provides a function that
return an onject(Python data structure)
represent by a JSON string
"""

import json


def from_json_string(my_str):
    """
    this func returns an onject represented by
    a JSON string
    """
    return json.loads(my_str)
