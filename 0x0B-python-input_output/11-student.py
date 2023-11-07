#!/usr/bin/python3
import json


class Student:
    """
    Defines a Student with attributes first_name, last_name, and age.
    """

    def __init(self, first_name, last_name, age):
        """
        Initializes a Student object with the given attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is provided, it retrieves only the specified attributes.
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a given dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
