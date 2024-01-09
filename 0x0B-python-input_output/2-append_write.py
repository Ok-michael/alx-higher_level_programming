#!/usr/bin/python3
""" this module contains a function that appends to a file """


def append_write(filename="", text=""):
    """ appends `text` to `filename` """
    with open(filename, 'a') as file:
        return file.write(text)
