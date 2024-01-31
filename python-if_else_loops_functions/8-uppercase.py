#!/usr/bin/python3
def uppercase(str):
    for upper in range(str):
        if "a" <= upper <= "z":
            print("{}".format(chr(upper - ord("a") + ord("A")), end=""))
        print(chr(upper), end="")
