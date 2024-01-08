#!/usr/bin/python3

""" represent an empty class """


class BaseGeometry:
    """ BaseGeometry class"""

    def area(self):
        """
        area calculation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
