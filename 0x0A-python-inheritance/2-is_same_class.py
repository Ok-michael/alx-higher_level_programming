#!/usr/bin/python3
""" this module has a function that checks if an object is an
    instance of the specified class"""


def is_same_class(obj, a_class):
    """ checkss if obj is an instance of a_class """
    if type(obj) is not a_class:
        return False
    return (isinstance(obj, a_class))
