#!/usr/bin/python3
"""
Contains the definition of 'Rectangle' class.
"""


class Rectangle:
    """
    Class that represents a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle object.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves width property.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width property.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Retrieves height property.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height property.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a human-readable representation of rectangle.
        """
        str = ''
        for x in range(self.height):
            for y in range(self.width):
                str += '#'
            if x < (self.height - 1):
                str += '\n'
        return str
