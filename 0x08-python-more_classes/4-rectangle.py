#!/usr/bin/python3
"""Defining a Rectangle of class."""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Representing the rectangle with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recte = []
        for v in range(self.__height):
            [recte.append('#') for j in range(self.__width)]
            if v != self.__height - 1:
                recte.append("\n")
        return ("".join(recte))

    def __repr__(self):
        """Return the string representation of Rectangle."""
        recte = "Rectangle(" + str(self.__width)
        recte += ", " + str(self.__height) + ")"
        return (recte)
