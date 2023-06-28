#!/usr/bin/python3
"""This module contains a class that represents a square."""


class Square:
    """This class that represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """
        This functin initalizes the square.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): the position of the square. Defaults to (0, 0).
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (
            type(position) is not tuple or
            len(position) != 2 or
            not all((type(number) is int) for number in position) or
            not all(number >= 0 for number in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """This function gets the private instance attribute: position."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        This function sets the private instance attribute: position.

        Args:
            value (int): The positon of a square.
        """
        if (
            type(value) is not tuple or
            len(value) != 2 or
            not all((type(number) is int) for number in value) or
            not all(number >= 0 for number in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This function returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """This function prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
            return
        for r in range(0, self.__position[1]):
            print()
        for r in range(0, self.__size):
            for c in range(0, self.__position[0]):
                print(end=" ")
            for c in range(0, self.__size):
                print("#", end="")
            print()

    def __eq__(self, other):
        """This function defines the == comparator based on the square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """This function defines the != comparator based on the square area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """This function defines the > comparator based on the square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """This function defines the >= comparator based on the square area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """This function defines the < comparator based on the square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """This function defines the <= comparator based on the square area."""
        return self.area() <= other.area()

    def __str__(self):
        """
        This function returns a human-readable
        representation of the square with the character #.
        """
        str = ""
        if self.__size == 0:
            return str
        for r in range(0, self.__position[1]):
            str += "\n"
        for r in range(0, self.__size):
            for c in range(0, self.__position[0]):
                str += " "
            for c in range(0, self.__size):
                str += "#"
            if (r < self.__size - 1):
                str += "\n"
        return str
