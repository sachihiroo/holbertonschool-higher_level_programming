#!/usr/bin/python3
"""
function that appends a string at the end of a text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends the given text to a file
    """
    with open(filename, "a") as f:
        n = f.write(text)
        return n
