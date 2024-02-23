#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method: def
        integer_validator(self, name, value): that validates value

        Args:
            name (str): The name .
            value (int): The parameter.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
