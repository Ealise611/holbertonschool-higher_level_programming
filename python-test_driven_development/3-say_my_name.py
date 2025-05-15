#!/usr/bin/python3
"""
This module provides a simple function to print a person's full name.

The function takes a first name and an optional last name,
validates their types, and prints the full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a full name in the format: My name is <first name> <last name>.

    Args:
        first_name (str): The person's first name.
        last_name (str, optional): The person's last name. Defaults to "".

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
