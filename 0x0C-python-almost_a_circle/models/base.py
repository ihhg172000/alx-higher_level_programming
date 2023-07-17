#!/usr/bin/python3
"""
Contains the definition of 'Base' class.
"""
import json


class Base:
    """
    Definition of 'Base' class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes Base instance.
        """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        with open(f"{cls.__name__}.json", "w") as file:
            dicts = []
            for obj in list_objs:
                dicts.append(
                    json.loads(cls.to_json_string(obj.to_dictionary()))
                )
            json.dump(dicts, file)
