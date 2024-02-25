#!/usr/bin/python3
"""
JSON USAGE
"""
import json


def from_json_string(my_str):
    """ return an obj represented by a JSON string"""
    return json.loads(my_str)
