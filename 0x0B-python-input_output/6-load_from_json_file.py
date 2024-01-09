#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”:

    You must use the with statement
    You don’t need to manage exceptions
    if the JSON string doesn’t represent an object.
    You don’t need to manage file permissions / exceptions.
    """
    with open(filename) as f:
        return json.load(f)
