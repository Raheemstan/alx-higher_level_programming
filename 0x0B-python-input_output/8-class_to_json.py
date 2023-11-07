#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description of a class instance with serializable attributes.
"""


def class_to_json(obj):
    """
    Return the dictionary description of a class instance with serializable attributes.

    :param obj: An instance of a class.
    :return: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
