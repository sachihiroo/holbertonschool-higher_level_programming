#!/usr/bin/python3
def no_c(my_string):
    text = ""
    for i in my_string:
        if i not in ["c", "C"]:
            text = text + i
    return text
