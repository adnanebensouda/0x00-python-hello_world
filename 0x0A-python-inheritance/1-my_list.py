#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implement sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascend order."""
        print(sorted(self))
