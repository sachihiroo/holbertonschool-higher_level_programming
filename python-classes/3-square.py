#!/usr/bin/python3
"""
"Empty Classes" are classes that don't have any attributes or methods,
but they can still  be used as placeholders for future development.
"""


class Square:
    """A class representing a square.
    Attributes:
    - size: int
        The size of the square.

    Methods:
    - __init__(self, size=0):
        Constructor to instantiate the Square class.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Verifying if the size is greater than or equal to 0
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    # Public instance method
    def area(self):
        """Returns the area of the square."""
        return self.__size**2

    pass
