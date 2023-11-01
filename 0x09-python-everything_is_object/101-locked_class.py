#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent user from instantiating new LockClass attribute
    for anything attribute call 'first_name'.
    """

    __slots__ = ["first_name"]
