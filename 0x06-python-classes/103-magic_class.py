#!/usr/bin/python3
"""
MagicClass class to mimic a Python bytecode.
"""

import math

class MagicClass:
    """
    MagicClass class that mimics a Python bytecode.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (float, optional): The radius of the circle. Defaults to 0.
        
        Raises:
            TypeError: If radius is not a number (float or integer).
        """
        self.radius = radius

    @property
    def radius(self):
        """
        Retrieve the radius of the circle.

        Returns:
            float: The radius of the circle.
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Set the radius of the circle.

        Args:
            value (float): The radius of the circle.

        Raises:
            TypeError: If value is not a number (float or integer).
        """
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
