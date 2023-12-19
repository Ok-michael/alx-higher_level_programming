#!/usr/bin/python3
"""
    Square - this program defines a square with some useful methods like
    __init__(), area() etc. It also handles of valuee exceptions upon
    object instantiations such as TypeError, and negative numbers.
"""


class Square:
    """
        Square - this program defines a square with some useful methods like
        __init__(), area() etc. It also handles of valuee exceptions upon
        object instantiations such as TypeError, and negative numbers.
    """

    def __init__(self, size=0):
        """
            __inti__ - this method is responsible for the configurations of
            each newly created objects and also handle some possible
            exceptions
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            area - this method returns the area of the square object
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
            size - this getter function returns the size of the object
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
            size - this overloaded version acts as the setter and rather
            sets the size to the value provided
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
