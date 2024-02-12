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
    - size: property
        Getter method to retrieve the size of the square.
    - size: setter
        Setter method to set the size of the square.
    - __init__(self, size=0):
        Constructor to instantiate the Square class.
    """

    def __init__(self, size=0, position=(0, 0)):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Verifying if the size is greater than or equal to 0
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("Position must be a tuple with two integers.")
        self.position = position

    # Property accessor methods (getter and setter)
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    # Public instance method
    def area(self):
        """Returns the area of the square."""
        return self.__size**2

    # Adding print method
    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.position[1]):
                  print()
            for j in range(self.position[0], self.position[0]+self.__size):
                       print(" " * self.position[0] + "#" * self.__size)
    pass
