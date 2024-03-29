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
        Writes the JSON string representation of list_objs to a file.
        """
        with open(f"{cls.__name__}.json", "w") as file:
            dicts = []
            if type(list_objs) is list:
                for obj in list_objs:
                    dicts.append(
                        json.loads(cls.to_json_string(obj.to_dictionary()))
                    )
            json.dump(dicts, file)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            obj = Rectangle(1, 1)
        if cls.__name__ == "Square":
            obj = Square(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        try:
            with open(f'{cls.__name__}.json', 'r') as file:
                dicts = cls.from_json_string(file.read())
                objts = []
                for dict in dicts:
                    objts.append(cls.create(**dict))
                return objts
        except FileNotFoundError:
            return []
