#!/usr/bin/python3
"""
- function that writes a string to a text file
(UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, "w") as f:
        n = f.write(text)
        return n
