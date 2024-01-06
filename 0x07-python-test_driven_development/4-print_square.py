#!/usr/bin/python3

def print_square(size):
    """
    print a square

    Parametres:
    size (int): the size of the squae
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
