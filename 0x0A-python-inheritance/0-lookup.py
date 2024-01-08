#!/usr/bin/python3

def lookup(obj):
    """
    returns the list of available attributes and methods of an object:

    Parameters:
    obj (obj): object

    Return:
    list object

    """

    return [att for att in (dir(obj))]
