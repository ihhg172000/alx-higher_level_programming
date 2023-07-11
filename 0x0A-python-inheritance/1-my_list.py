#!/usr/bin/python3
"""Contains the definition of 'MyList' class."""


class MyList(list):
    """Class that extends 'list' class."""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
