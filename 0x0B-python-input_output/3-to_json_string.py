#!/usr/bin/python3

import json

"""
This module contains a function that returns the JSON representation of an object (string).
"""


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.

    :param my_obj: The object to be converted to JSON.
    :return: A JSON string representation of the object.
    """
    return json.dumps(my_obj)
