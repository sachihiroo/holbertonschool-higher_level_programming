#!/usr/bin/python3
def uppercase(str):
    for upper in range(str):
        if 'a' <= upper  <= 'z':
            print(chr(upper - ord('a') + ord('A')), end ="")
        else:
            print(chr(upper),end="")
