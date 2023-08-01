#!/usr/bin/python3
"""Define a JSON file reading function."""
import json


def load_from_json_file(filename):
    """Create Python object from JSON file."""
    with open(filename) as f:
        return json.load(f)
