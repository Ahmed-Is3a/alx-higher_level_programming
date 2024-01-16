#!/usr/bin/python3
""" retpresent square model """
from rectangle import Rectangle


class Square(Rectangle):
    """ represent Square class that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args:
            if len(args) > 0:
                self.id = args[0] if args[0] is not None else self.id
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """ returns the dictionary representaion """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
