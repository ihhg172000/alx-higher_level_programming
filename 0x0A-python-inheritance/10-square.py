#!/usr/bin/python3
"""Contains the definition of 'Square' class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of `Square` class."""
    def __init__(self, size):
        """Initializes a Square instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
