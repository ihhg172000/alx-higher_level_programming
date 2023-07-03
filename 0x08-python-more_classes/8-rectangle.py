#!/usr/bin/python3
"""
Contains the definition of 'Rectangle' class.
"""


class Rectangle:
    """
    Class that represents a rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle object.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """
        Returns a human-readable representation of rectangle.
        """
        s = ''
        if self.width == 0 or self.height == 0:
            return s
        for x in range(self.height):
            for y in range(self.width):
                s += str(self.print_symbol)
            if x < (self.height - 1):
                s += '\n'
        return s

    def __repr__(self):
        """
        Returns representation of rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Called after an object's garbage collection occur.
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
