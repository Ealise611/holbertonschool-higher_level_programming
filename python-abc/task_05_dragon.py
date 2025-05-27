#!/usr/bin/python3
"""
Design two mixin classes, SwimMixin and FlyMixin
each equipped with methods swim and fly respectively.
Next, construct a class Dragon that inherits from both these mixins.
Your aim is to show that a Dragon instance can both swim and fly.
"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
