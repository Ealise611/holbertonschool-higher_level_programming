#!/usr/bin/python3
"""
this module has class CountedIterator that extends
the built-in iterator obtain from the iter
"""


class CountedIterator():
    """
    CountedIterator that extends the built-in
    iterator obtained from iter function
    """
    def __init__(self, iterables):
        self.iterables = iterables
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        if self.count < len(self.iterables):
            value = self.iterables[self.count]
            self.count += 1
            return value
        else:
            raise StopIteration
