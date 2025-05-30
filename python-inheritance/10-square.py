#!/usr/bin/python3
"""
Square module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from Rectangle
    width and height must be private
    must be positive number validate by integer_validator
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
