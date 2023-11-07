#!/usr/bin/python3
"""
This module contains a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number of characters added.

    :param filename: The name of the file to append to (default is an empty string).
    :param text: The text to append to the file (default is an empty string).

    :return: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
