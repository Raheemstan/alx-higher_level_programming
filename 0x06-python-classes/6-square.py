#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size, size validation, and methods to access, update, and print the square with coordinates."""
class Square:
    """A class representing a square with a size and position."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance with optional size and position.
        
        Args:
            size (int, optional): The size of the square.
            position (tuple of int, optional): The position of the square.
        
        Raises:
            TypeError: If size is not an integer or position is not a tuple of two positive integers.
            ValueError: If size is less than 0 or if the elements of position are less than 0.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the size of the square.
        
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        
        Args:
            value (int): The size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square.
        
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        
        Args:
            value (tuple of int): The position of the square.
        
        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' characters at the specified position."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
