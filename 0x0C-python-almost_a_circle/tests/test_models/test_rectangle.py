#!/usr/bin/python3
"""
Contains the unittest for 'rectangle' module.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unit test for 'Rectangle' class.
    """
    def test_type_validation(self):
        """
        Test integer validation."""
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1.5, 1)

        self.assertTrue("width must be an integer", err.exception)

        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1, 'hello')

        self.assertTrue("height must be an integer", err.exception)

        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1, 1, True, 10)

        self.assertTrue("x must be an integer", err.exception)

        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1, 1, 1, [1, 10])

        self.assertTrue("y must be an integer", err.exception)

    def test_value_validation(self):
        """
        Test value validation.
        """
        with self.assertRaises(ValueError) as err:
            rect = Rectangle(0, 1)

        self.assertTrue("width must be > 0", err.exception)

        with self.assertRaises(ValueError) as err:
            rect = Rectangle(1, 1, -1, 10)

        self.assertTrue("x must be >= 0", err.exception)


if __name__ == '__main__':
    """main"""
    unittest.main()
