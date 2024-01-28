#!/usr/bin/python3
for ch in range(97, 123):
    if ch == "e" or ch == "q":
        continue
print("{}".format(chr(ch)), end="")
