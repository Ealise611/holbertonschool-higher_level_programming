#!/usr/bin/python3
"""
This module writes a string to a text file
and return number of characters written
"""


def write_file(filename="", text=""):
    """
    this function write file and return
    num of characters
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        char_count = 0
        for line in filename:
            char_count += len(line)
        return char_count
