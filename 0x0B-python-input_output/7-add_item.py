#!/usr/bin/python3
"""
Adds all arguments to a Python list,
and then save them to a file.
"""
from sys import argv
import json


with open('add_item.json', 'w') as file:
    json.dump(argv[1:], file)
