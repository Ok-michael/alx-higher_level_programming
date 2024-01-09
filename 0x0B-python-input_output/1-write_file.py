#!/usr/bin/python3
""" this module has a func that writes to a file """


def write_file(filename="", text=""):
    """ writes `text` to `filename` """
    with open(filename, 'w') as p:
        return (p.write(text))
