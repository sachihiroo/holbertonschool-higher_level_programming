#!/usr/bin/python3
"""
JSON USAGE
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    with open(filename, "wt") as f:
        json.dump(my_obj, f)
