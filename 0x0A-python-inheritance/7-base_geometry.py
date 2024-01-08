#!/usr/bin/python3

""" base goemetry calculation modulal """


class BaseGeometry:
    """ BaseGeometry class - calculates the geomety"""

    def area(self):
        """
        calculates the area of the geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator: validates if the given value is an int
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
