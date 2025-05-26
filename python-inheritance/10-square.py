#!/usr/bin/python3
"""
Rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
    width and height must be private
    must be positive number validate by integer_validator
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
