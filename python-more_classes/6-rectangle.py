#!/usr/bin/python3
"""
"Empty Classes" are classes that don't have any attributes or methods,
but they can still  be used as placeholders for future development.
"""


class Rectangle:
    """A class representing a Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        "Retu"
        return self.height * self.width

    def perimeter(self):
        "Return the perimeter of this rectangle."
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print("")
        return ""

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
