""" represent Rectangle model"""


Base = __import__('base').Base


class Rectangle(Base):
    """ represent Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle class constractor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter function """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter function """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter function """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter functon """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter function """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter functon """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter function """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter functon """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """  public method that returns the area value"""
        return self.height * self.width

    def display(self):
        """
        public method that prints in stdout the Rectangle instance
        with the character # - you don’t need to handle x and y here.
        """
        s = ""
        if self.width == 0 or self.height == 0:
            return ""
        s += "\n" * self.y
        for i in range(self.height - 1):
            s += (" " * self.x + "#" * self.__width + "\n")
        s += (" " * self.x + "#" * self.__width)
        print(s)

    def __str__(self):
        """ magic method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """ assigns an argument to each attribute """
        if len(args) > 0:
            self.id = args[0] if args[0] is not None else self.id
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
