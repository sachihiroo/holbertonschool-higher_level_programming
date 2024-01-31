#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if "a" <= upper <= "z":
            print("{}".format(upper=chr(ord(upper) - 32)), end="")
    print()
