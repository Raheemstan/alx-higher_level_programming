#!/usr/bin/python3
"""
Square class for comparing square instances
"""

class Square:
    """
    Square class defines a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Check if two squares are equal based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares have the same area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Check if two squares are not equal based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares have different areas, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Check if one square is less than the other based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square has a smaller area than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Check if one square is less than or equal to the other based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square has a smaller or equal area than the other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Check if one square is greater than the other based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square has a larger area than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Check if one square is greater than or equal to the other based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square has a larger or equal area than the other, False otherwise.
        """
        return self.area() >= other.area()
