#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list = my_list.copy()
    if my_list and -1 < idx < len(my_list) and element:
        my_list[idx] = element
    return my_list
