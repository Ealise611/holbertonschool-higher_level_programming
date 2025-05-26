#!/usr/bin/python3
"""
Rectangle module
"""

class BaseGeometry:
    """
    raise exception message
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
    width and height must be private
    must be positive number validate by integer_validator
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
