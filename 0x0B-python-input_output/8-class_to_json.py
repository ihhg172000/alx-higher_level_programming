#!/usr/bin/python3
"""Contains the definition of 'class_to_json' function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure."""
    return obj.__dict__
