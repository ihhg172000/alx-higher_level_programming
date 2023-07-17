#!/usr/bin/python3
"""
Contains the definition of 'Square' class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes 'Square' instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a human-readable representation of 'Rectangle'.
        """
        return (f'[Square] ({self.id}) {self.x}/{self.y} ' +
                f'- {self.width}')

    @property
    def size(self):
        """
        Retrieves 'size' property. aka 'width' or 'height'.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets 'size' property aka 'width' and 'height'.
        """
        self.width = value
        self.height = value
