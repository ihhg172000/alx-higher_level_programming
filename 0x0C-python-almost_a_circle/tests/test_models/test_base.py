#!/usr/bin/python3
"""
Contains the unittest for 'base' module.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Unit test for 'Base' class.
    """
    def test_id(self):
        """
        Test id.
        """
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 10)
        self.assertEqual(b3.id, 2)


if __name__ == '__main__':
    """main"""
    unittest.main()
