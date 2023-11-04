#!/usr/bin/python3
"""
This module defines a class Rectangle.
"""


class Rectangle:
    """
    Rectangle class represents a rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#' characters.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str("#" * self.__width)] * self.__height)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: String representation of the Rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor method that prints a message when a Rectangle object is deleted.
        """
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two Rectangle objects and returns the one with the greater area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The Rectangle with the greater area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
