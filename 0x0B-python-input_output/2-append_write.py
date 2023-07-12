#!/usr/bin/python3
"""Contains the definition of 'append_write' function."""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file.

    Return:
        the number of characters added.
    """
    with open(filename, 'a') as file:
        return file.write(text)
