#!/usr/bin/python3

class Square:
    """
    Defines a class Square with a private instance attribute size and position.
    Includes size and position validation, a method to calculate the area, and methods to print the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with a size and position.
        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter method for the position attribute.
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.
        Args:
            value (tuple): The position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) for x in value) or any(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Prints the square using '#' characters with the specified position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
