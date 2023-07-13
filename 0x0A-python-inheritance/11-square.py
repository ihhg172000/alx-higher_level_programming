#!/usr/bin/python3
"""Contains the definition of 'Square' class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of `Square` class."""
    def __init__(self, size):
        """Initializes a Square instance"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a human-readable representation of Square instance"""
        return f"[Square] {self.__size}/{self.__size}"
