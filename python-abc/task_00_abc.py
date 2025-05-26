#!/usr/bin/python3
"""
This is an animal module will have two subclasses
dog and cat and implemet sount method in each subclasses
will return "bark" and "meow"
"""


from abc import ABC, abstractclassmethod

class Animal(ABC):
    """
    class animal have two subclasses
    """
    @abstractclassmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return("Bark")

class Cat(Animal):
    def sound(self):
        return("Meow")

