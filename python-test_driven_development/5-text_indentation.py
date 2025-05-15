#!/usr/bin/python3
"""
This module defines a function that prints text with formatting.

The function inserts two new lines after
each '.', '?' and ':' in the input text.
It also ensures that no printed line has leading or trailing spaces.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    for i in text:
        new_text += i
        if i in ".?:":
            print(new_text.strip())
            print()
            new_text = ""
    if new_text.strip():
        print(new_text.strip(), end="")
