#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represeningt a rectangle.

    Attributes:
        number_of_instances (int): number of Rectangle instance.
        print_symbol (any): The symbol used for string representating.
    """

    number_of_instance = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instance += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
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
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Representing the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recte = []
        for v in range(self.__height):
            [recte.append(str(self.print_symbol)) for j in range(self.__width)]
            if v != self.__height - 1:
                recte.append("\n")
        return ("".join(recte))

    def __repr__(self):
        """Return the string representing of the Rectangle."""
        recte = "Rectangle(" + str(self.__width)
        recte += ", " + str(self.__height) + ")"
        return (recte)

    def __del__(self):
        """Print a message every deletion a Rectangle."""
        type(self).number_of_instance -= 1
        print("Bye rectangle...")
