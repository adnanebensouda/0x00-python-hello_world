#!/usr/bin/python3
""" defines a square """


class Square:
    """ this is square with private instance attribute size """

    def __init__(self, size=0):
        """
        initializes square
        Args:
            size: this is size of side of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        finding area of square
        Returns:
            the all area of the square
        """

        return self.__size ** 2
