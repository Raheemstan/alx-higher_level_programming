#!/usr/bin/python3
"""
This module contains a function that reads a text file (UTF-8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Read a text file and print its content to stdout.

    :param filename: The name of the file to read (default is an empty string).
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
