#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    line = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            line = line + 1
    except IndexError:
        pass
    finally:
        print()
    return line
