#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a text file.

The file is opened with UTF-8 encoding and its
contents are printed to standard output.
If the file does not exist or cannot be opened, an exception will be raised.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
    filename (str): The name of the file to read. Defaults to an empty string.

    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
