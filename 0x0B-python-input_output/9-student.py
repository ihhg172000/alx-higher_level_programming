#!/usr/bin/python3
"""Contains the definition of 'Student' class."""


class Student:
    def __init__(self, first_name, last_name, age):
        """initializes Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
