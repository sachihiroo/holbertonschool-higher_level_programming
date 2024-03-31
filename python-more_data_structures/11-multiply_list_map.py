#!/usr/bin/python3
"""
Write a function that returns a list with all
values multiplied by a number
"""


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda valx: valx*number, my_list))