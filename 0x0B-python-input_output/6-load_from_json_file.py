#!/usr/bin/python3
"""Contains the definition of 'load_from_json_file' function."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”."""
    with open(filename, 'r') as file:
        return json.load(file)
