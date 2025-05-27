#!/usr/bin/python3
"""
Module using class VerboseList that extends
the Python list class and provide custom behaviours
"""


class VerboseList(list):

    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, x):
        print(f"Extended the list with [{len(x)}] items.")
        super().extend(x)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"poped [{item}] from the list.")
        return item
