#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    :param filename: The name of the file to write to (default is an empty string).
    :param text: The text to write to the file (default is an empty string).

    :return: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
