#!/usr/bin/python3

import json

"""
This module contains a function that returns the JSON representation of an object (string).
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    :param my_obj: The Python object to be converted to JSON.

    :return: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
