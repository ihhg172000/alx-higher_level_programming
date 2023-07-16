#!/usr/bin/python3
"""
Contains the definition of 'Rectangle' class.
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes 'Rectangle' instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieves 'width' property.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets 'width' property.
        """
        self.__integer_validation(value, 'width')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        Retrieves 'height' property.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets 'height' property.
        """
        self.__integer_validation(value, 'height')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        Retrieves 'x' property.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets 'x' property.
        """
        self.__integer_validation(value, 'x')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        Retrieves 'y' property.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets 'y' property.
        """
        self.__integer_validation(value, 'y')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__y = value

    @staticmethod
    def __integer_validation(value, attr_name):
        """
        Integer validation.
        """
        if type(value) is not int:
            raise TypeError(f'{attr_name} must be an integer')
