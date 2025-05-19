#!/usr/bin/python3
"""
This module defines an empty Square class
"""


class Square:
    """
    this square class
    """
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        result = self.__size ** 2
        return result
