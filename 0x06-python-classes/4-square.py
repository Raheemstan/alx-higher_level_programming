#!/usr/bin/python3

class Square:
    """
    Defines a class Square with a private instance attribute size.
    Includes size validation, a method to calculate the area, and a property for size.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a size.
        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        Args:
            value (int): The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
