#!/usr/bin/python3
"""returns True if the object is exactly an instance of cls, False otherwise."""


def is_same_class(obj, a_class):
    """check if is exactly an instance"""
    if type(obj) == a_class:
        return True
    else:
        return False
