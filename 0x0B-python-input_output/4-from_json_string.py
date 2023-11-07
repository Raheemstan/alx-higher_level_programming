#!/usr/bin/python3

import json

"""
This module contains a function that returns an object (Python data structure) represented by a JSON string.
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    :param my_str: The JSON string to be converted to a Python object.

    :return: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
