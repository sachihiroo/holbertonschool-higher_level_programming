#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in range(len(my_list)):
        if my_list[idx] < 0:
            return None
        if idx < (len(my_list)):
            return my_list[idx]
        return None
