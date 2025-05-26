#!/usr/bin/python3
"""
BaseGeometry module
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
