#!/usr/bin/python3
import json

"""
This module contains a function that writes an object to a text file using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    :param my_obj: The Python object to be saved to the file.
    :param filename: The name of the file to save the object.

    You must use the with statement
    You don’t need to manage exceptions if the object can’t be serialized.
    You don’t need to manage file permission exceptions.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
