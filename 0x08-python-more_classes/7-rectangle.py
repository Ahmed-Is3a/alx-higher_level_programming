#!/usr/bin/python3

""" represent a class Rectangle """


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    - number_of_instances (int): class attribute
    - print_symbol (str): symbol '#'
    Methods:
    - __init__(self, width=0, height=0): Initializes a new Rectangle instance.
    - width(self): retrive the width value
    - width(self, value): set value
    - height(self): retrive height value
    - height(self, value): set height value
    - area(self): calculates the area
    - perimeter(self): calculates the perimeter
    - __str__(self): string representation of class object
    - __repr__(self): Returns a string representation of the rectangle.
    - __del__(): distructor, runs when an object is deleted
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        # if self.__width == 0 or self.__height == 0:
        #     return ""
        # return (str(self.print_symbol) * self.__width + "\n") * self.__height
        s = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height - 1):
            s = s + (str(self.print_symbol) * self.__width + "\n")
        s = s + (str(self.print_symbol) * self.__width)
        return s

    def __repr__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
