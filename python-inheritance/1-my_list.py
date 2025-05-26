#!/usr/bin/python3
"""
This module defines a custom list subclass called MyList.

The MyList class inherits from the built-in list type and adds a public
instance method `print_sorted` that prints the list's elements in ascending order.

All elements in the list are assumed to be integers.
"""

class MyList(list):
    """
    A subclass of the built-in list type that provides an additional method
    to print the elements of the list in sorted order.

    This class inherits all the functionality of the standard Python list
    and adds a custom method for displaying a sorted version of the list.
    """
    def print_sorted(self):
        result = sorted(self)
        print(result)
