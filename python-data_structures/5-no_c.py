#!/usr/bin/python3
def no_c(my_string):
    for i in range(my_string):
        if my_string[i] != "C" or my_string[i] != "c":
            print("{}".format(my_string[i]), end="")
