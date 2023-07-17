#!/usr/bin/python3
"""
Contains the definition of 'Base' class.
"""


class Base:
    """
    Definition of 'Base' class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes Base instance.
        """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
