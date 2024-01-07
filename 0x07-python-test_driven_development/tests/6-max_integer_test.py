#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_positive(self):
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5, "Max integer should be 5")

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -3, -5, -2, -4]), -1, "Max integer should be -1")

    def test_max_integer_mixed(self):
        self.assertEqual(max_integer([-1, 3, 0, -2, 5]), 5, "Max integer should be 5")

    def test_max_integer_duplicate(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5, "Max integer should be 5")

    def test_max_integer_single_element(self):
        self.assertEqual(max_integer([42]), 42, "Max integer should be 42")

    def test_max_integer_large_list(self):
        self.assertEqual(max_integer(list(range(10**6))), 999999, "Max integer should be 999999")


if __name__ == "__main__":
	unittest.main()