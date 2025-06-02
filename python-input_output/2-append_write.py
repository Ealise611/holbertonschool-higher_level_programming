#!/usr/bin/python3
"""
This module append a string to a end of text file
and return number of characters added
"""


def append_write(filename="", text=""):
    """
    this func append to file and return
    number of characters append
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
