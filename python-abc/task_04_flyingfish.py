#!/usr/bin/python3
"""
This module is Construct a FlyingFish class that
inherits from both a Fish class and a Bird class.
Within FlyingFish, override methods from both parents.
The goal is to comprehend multiple inheritance and
how Python determines method resolution order.
"""


class Fish:
    """
    fish class
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """
    Bird class
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
