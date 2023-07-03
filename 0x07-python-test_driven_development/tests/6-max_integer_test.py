#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Tests max_integer function.
    """
    def test_empty_list(self):
        """
        Test empty list.
        """
        result = max_integer([])
        self.assertEqual(result, None)

    def test_all_integers(self):
        """
        Test all integers.
        """
        result = max_integer([1, 2, 3])
        self.assertEqual(result, 3)

    def test_repeating_a_number(self):
        """
        Test repeating a number.
        """
        result = max_integer([1, 2, 3, 3])
        self.assertEqual(result, 3)

    def test_all_floats(self):
        """
        Test all floats.
        """
        result = max_integer([1.5, 2.5, 3.5])
        self.assertEqual(result, 3.5)

    def test_mixed_integers_and_floats(self):
        """
        Test mixed integers and floats.
        """
        result = max_integer([1, 2, 3.5])
        self.assertEqual(result, 3.5)

    def test_string(self):
        """
        Test string.
        """
        result = max_integer('abc')
        self.assertEqual(result, 'c')

    def test_empty_string(self):
        """
        Test empty string.
        """
        result = max_integer('')
        self.assertEqual(result, None)
