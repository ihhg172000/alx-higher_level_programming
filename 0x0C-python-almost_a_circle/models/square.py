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

    def update(self, *args, **kwargs):
        """
        Updates the 'Square' instance.
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.
        """
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'size': self.size}

    def __str__(self):
        """
        Returns a human-readable representation of 'Square'.
        """
        return (f'[Square] ({self.id}) {self.x}/{self.y} ' +
                f'- {self.width}')
