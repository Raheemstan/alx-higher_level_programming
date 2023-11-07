#!/usr/bin/python3
import json

"""
This module contains a function that adds an item to a JSON file.
"""


def add_item(filename, item):
    """
    Add an item to a JSON file.

    :param filename: The name of the JSON file.
    :param item: The item to add to the file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(item)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)
