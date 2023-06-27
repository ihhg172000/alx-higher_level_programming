#!/usr/bin/python3
"""This module contains a class that represents a square."""


class Square:
    """This class that represents a square."""
    def __init__(self, size=0):
        """
        This functin initalizes the square.

        Args:
            size (int): The size of a square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """This function gets the private instance attribute: size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        This function sets the private instance attribute: size.

        Args:
            value (int): The size of a square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This function returns the area of the square."""
        return self.__size ** 2
