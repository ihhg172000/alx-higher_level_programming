#!/usr/bin/python3
"""Contains the definition of 'Rectangle' class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of `Rectangle` class."""
    def __init__(self, width, height):
        """Initializes a Rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a human-readable representation of Rectangle instance"""
        return f"[Rectangle] {self.__width}/{self.__height}"
