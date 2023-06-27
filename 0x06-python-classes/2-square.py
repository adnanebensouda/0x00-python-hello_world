#!/usr/bin/python3

"""Defination a class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initialize the new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(int, size):
            raise TypeError("size must be an integer")
        elif 0 > size:
            raise ValueError("size must be >= 0")
        self.__size = size
