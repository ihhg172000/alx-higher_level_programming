#!/usr/bin/python3
"""Contains the definition of 'save_to_json_file' function."""
import json


def save_to_json_file(my_str, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, 'w') as file:
        json.dump(my_str, file)
