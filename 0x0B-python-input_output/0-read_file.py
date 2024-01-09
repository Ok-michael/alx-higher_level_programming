#!/usr/bin/python3
""" this module has a function that reads from a text file """


def read_file(filename=""):
    """ reads the passed text file """
    with open(filename, 'r') as f:
        print(f.read(), end='')
