#!/usr/bin/python3
"""Define string JSON function."""
import json


def to_json_string(my_obj):
    """Return JSON representation of a string object."""
    return json.dumps(my_obj)
