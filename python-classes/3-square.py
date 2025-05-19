#!/usr/bin/python3
"""
This module defines an empty Square class
"""


class Square:
    """
    this square class
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):

        result = self.__size ** 2
        return result
