#!/usr/bin/python3
"""
    This module defines a function that returns the list
    of available attributes and methods of an object
"""


def lookup(obj):
    """
        lookup: a function that returns the list of all
        available attributes and methods of an objec
        Return: it returns the list of all available attri-\
                butes and method
        Args: obj -> an object from any class whatsoever
    """
    return (dir(obj))
