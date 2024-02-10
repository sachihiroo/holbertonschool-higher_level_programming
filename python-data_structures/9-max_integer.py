#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    largest_number = None
    for number in my_list:
        if largest_number is None or largest_number < number:
            largest_number = number
    return largest_number
