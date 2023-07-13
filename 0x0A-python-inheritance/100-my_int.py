#!/usr/bin/python3
"""Contains the definition of 'MyInt' class."""


class MyInt(int):
    """Definition of `MyInt` class."""
    def __eq__(self, other):
        """Inverts == operators"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Inverts != operators"""
        return int.__eq__(self, other)
