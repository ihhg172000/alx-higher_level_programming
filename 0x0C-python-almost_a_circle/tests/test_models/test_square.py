#!/usr/bin/python3
"""
Contains the unittest for 'square' module.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Unit test for 'Square' class.
    """
    def test_size(self):
        """
        Test size getter and setter
        """
        square = Square(10)
        self.assertEqual(square.size, 10)
        square.size = 5
        self.assertEqual(square.size, 5)

        with self.assertRaises(TypeError) as err:
            square.size = 1.5

        self.assertTrue(err.exception, 'width must be an integer')

        with self.assertRaises(ValueError) as err:
            square.size = -1

        self.assertTrue(err.exception, 'width must be > 0')
