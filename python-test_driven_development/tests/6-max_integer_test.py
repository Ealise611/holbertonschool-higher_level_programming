#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), )
    def test_single_element_list(self):
        self.assertEqual(max_integer([1]), 1)
    def test_positive_number(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_negative_number(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    def test_mixed_number(self):
        self.assertEqual(max_integer([-1, 2, -3, -4]), 2)
    def test_duplicate_number(self):
        self.assertEqual(max_integer([1, 1, -3, -4]), 1)
