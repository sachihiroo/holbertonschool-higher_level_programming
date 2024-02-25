#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """Reads a file"""
    with open(filename, "r") as f:
        r = f.read()
        print(r, end="")
