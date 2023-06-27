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

    def area(self):
        """This function returns the area of the square"""
        return self.__size ** 2
