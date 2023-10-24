#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size, size validation, and an area method."""
class Square:
    """A class representing a square with a size."""
    
    def __init__(self, size=0):
        """Initialize a new Square instance with optional size.
        
        Args:
            size (int, optional): The size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
