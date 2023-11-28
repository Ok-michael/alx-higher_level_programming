#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for character in str:
        if ord(character) in range(97, 123):
            new_str += chr(ord(character) - 32)
        else:
            new_str += character
    print("{:s}".format(new_str))
