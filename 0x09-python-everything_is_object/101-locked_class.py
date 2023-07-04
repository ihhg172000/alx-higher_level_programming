#!/usr/bin/python3
"""
Contains the definition of 'LockedClass' class.
"""


class LockedClass:
    """
    Class that prevents the user from creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']
