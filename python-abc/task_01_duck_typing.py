#!/usr/bin/python3
"""
This is a module with a Abstract class named Shape
with two abstract method area and perimeter
"""


from abc import ABC, abstractclassmethod
import math

class Shape(ABC):
    """
    class shape has two concrete classes
    circle and rectangle
    """

    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * self.radius * 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
