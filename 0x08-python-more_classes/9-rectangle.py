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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.

        Parameters:
        - rect_1 (Rectangle): The first rectangle.
        - rect_2 (Rectangle): The second rectangle.

        Returns:
        Rectangle: The rectangle with the greater or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size.

        Parameters:
        - size (int): The size of the square. Default is 0.

        Returns:
        Rectangle: A new Rectangle instance representing a square.
        """
        return cls(width=size, height=size)
