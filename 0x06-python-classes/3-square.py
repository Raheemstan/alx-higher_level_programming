#!/usr/bin/python3

class Square:
    """
    Defines a class Square with a private instance attribute size.
    Includes size validation and a method to calculate the area.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a size.
        Args:
            size (int): The size of the square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
