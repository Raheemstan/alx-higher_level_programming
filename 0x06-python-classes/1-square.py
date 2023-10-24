#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""
class Square:
    """A class representing a square with a size."""
    
    def __init__(self, size):
        """Initialize a new Square instance.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
