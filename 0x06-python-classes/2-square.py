#!/usr/bin/python3
"""
    Class Square - defines a square with one optional argument size
    it has a method __init__() which serves to initialize the objects
    once created
"""


class Square:
    """
        Square - A class that defines a square with just one method __init__()
    """

    def __init__(self, size=0):
        """
            this method helps initialize any object created
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
