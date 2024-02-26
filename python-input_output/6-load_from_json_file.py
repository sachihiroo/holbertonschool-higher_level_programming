#!/usr/bin/python3
"""
JSON USAGE
"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”."""
    with open(filename) as f:
        n = json.load(f)
    return n
