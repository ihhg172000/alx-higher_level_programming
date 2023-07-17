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

    def test_area(self):
        """
        Test area.
        """
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(4, 8)
        self.assertEqual(rect1.area(), 50)
        self.assertEqual(rect2.area(), 32)

    def test_update_args(self):
        """
        Test update using *args
        """
        rect = Rectangle(10, 20, 1, 1, 1)
        rect.update(10, 20, 40, 5, 5)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 40)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    def test_update_kwargs(self):
        """
        Test update using *kwargs
        """
        rect = Rectangle(10, 20, 1, 1, 1)
        rect.update(width=20, id=10, height=40, x=5, y=5)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 40)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)


if __name__ == '__main__':
    """main"""
    unittest.main()
