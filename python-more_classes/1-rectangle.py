#!/usr/bin/python3
"""
"Empty Classes" are classes that don't have any attributes or methods,
but they can still  be used as placeholders for future development.
"""


class Rectangle:
    """A class representing a Rectangle."""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    # Property accessor methods (getter and setter)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # Verifying if the width is greater than or equal to 0
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
    # Verifying if the height is greater than or equal to 0
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
