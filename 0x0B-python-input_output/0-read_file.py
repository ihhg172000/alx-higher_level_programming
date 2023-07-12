#!/usr/bin/python3
"""Contains the definition of 'read_file' function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r') as file:
        print(file.read(), end="")
