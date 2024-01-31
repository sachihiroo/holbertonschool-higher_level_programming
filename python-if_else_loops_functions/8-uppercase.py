#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if "a" <= upper <= "z":
            upper = chr(ord(upper) - 32)
            print("{}".format(upper), end="")
        print()
