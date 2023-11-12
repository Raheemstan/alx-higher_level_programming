#!/usr/bin/python3

"""Module for Base class"""
class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
