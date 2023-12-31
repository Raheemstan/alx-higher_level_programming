#!/usr/bin/python3
"""
This module defines a class Rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with the given width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str("#" * self.__width)] * self.__height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle in the form
        'Rectangle(width, height)' to be able to recreate a new instance
        by using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"
