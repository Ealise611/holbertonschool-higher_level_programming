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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        result = self.__size ** 2
        return result

    def my_print(self):
        if self.__size < 0 or self.__size == 0:
            print("")
        for i in range(self.__size):
            print('#' * self.__size)