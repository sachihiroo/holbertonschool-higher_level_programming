#!/usr/bin/python3
"""Add two integers. If only one argument is provided the other will be 98."""
def add_integer(a, b=98):

    """
    arguments: a, b
    Return: int
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    return (int(a)+int(b))
