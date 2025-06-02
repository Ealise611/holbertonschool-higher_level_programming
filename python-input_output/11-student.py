#!/usr/bin/python3
"""
This module has a class student
with first_name, last_name, age
"""


class Student:
    """
    this is a class defines student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                result = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        result[attr] = getattr(self, attr)
                        #set dictironary[key] = value
                return result
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
