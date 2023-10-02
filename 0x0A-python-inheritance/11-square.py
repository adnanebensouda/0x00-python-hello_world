#!/usr/bin/python3
"""Define a Rectangle sub class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
