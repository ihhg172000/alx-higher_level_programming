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

    def test_to_json_string(self):
        """
        Test to_json_string
        """
        jstr = Base.to_json_string(
                [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
            )
        self.assertEqual(
                jstr, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
                )
        jstr = Base.to_json_string(None)
        self.assertEqual(jstr, "[]")
        jstr = Base.to_json_string([])
        self.assertEqual(jstr, "[]")


if __name__ == '__main__':
    unittest.main()
