#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv

    num_args = len(argv)
    if num_args == 1:
        print("0 arguments.")
    elif num_args == 2:
        print("{} argument:".format(num_args - 1))
        print("argument 1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(num_args - 1))
    for i in range(1, num_args):
        print("{}: {}".format(i, argv[i]))
