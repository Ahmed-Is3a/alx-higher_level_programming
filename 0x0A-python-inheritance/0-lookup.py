#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object:

    Parameters:
    obj (obj): object

    Return:
    list object

    """

    return (dir(obj))
