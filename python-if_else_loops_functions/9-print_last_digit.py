#!/usr/bin/python3
def print_last_digit(number):
    digit = abs(number) % 10
    if digit > 9:
        print(number)
    elif 0 <= digit >= 9:
        print(number)
        return number
