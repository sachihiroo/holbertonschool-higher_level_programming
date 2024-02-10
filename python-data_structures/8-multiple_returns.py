#!/usr/bin/python3
def multiple_returns(sentence):
    frst_character = None
    length = 0
    if sentence:
        frst_character = sentence[0]
        length = len(sentence)
    return (length, frst_character)
