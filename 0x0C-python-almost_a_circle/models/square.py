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
