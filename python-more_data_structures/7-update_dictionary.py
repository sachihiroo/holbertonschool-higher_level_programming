#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        return a_dictionary
    else:
        a_dictionary[key] = value
        return a_dictionary
