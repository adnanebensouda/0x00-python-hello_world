#!/usr/bin/python3
"""Define a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsenting base geometry."""

    def area(self):
        """Not yet implement."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
