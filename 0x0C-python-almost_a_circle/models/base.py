#!/usr/bin/python3
""" represnt the base model"""


class Base:
    """ represent a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__ magic method runs when an object is created"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
