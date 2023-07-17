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
        Test 'size' getter and setter
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

    def test_update_args(self):
        """
        Test update using *args
        """
        square = Square(10, 1, 1)
        square.update(10, 20, 5, 5)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 5)

    def test_update_kwargs(self):
        """
        Test update using *kwargs
        """
        square = Square(10, 1, 1)
        square.update(size=20, id=10, x=5, y=5)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        """
        Test to_dictionary.
        """
        s1 = Square(10, 1, 5, 100)
        s1_dictionary = s1.to_dictionary()

        s2 = Square(1)
        s2.update(**s1_dictionary)

        self.assertEqual(s2.id, 100)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 5)


if __name__ == '__main__':
    unittest.main()
