#!/usr/bin/python3
import json

"""
This module contains a function that creates an object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    :param filename: The name of the JSON file.
    :return: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
