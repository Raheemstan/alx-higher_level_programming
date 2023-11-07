#!/usr/bin/python3
"""
This module contains a class Student that defines a student by first name, last name, and age.
"""


class Student:
    """
    This class defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
