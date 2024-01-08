#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    a function that returns True if the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False.

    Parameters:
    obj (obj): object
    a_class (class):  a class

    Returns:
    True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
