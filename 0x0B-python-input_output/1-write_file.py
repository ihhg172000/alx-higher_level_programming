#!/usr/bin/python3
"""Contains the definition of 'write_file' function."""


def write_file(filename="", text=""):
    """
    writes a string to a text file.

    Return:
        the number of characters written.
    """
    with open(filename, 'w') as file:
        return file.write(text)
