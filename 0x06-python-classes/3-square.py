#!/usr/bin/python3
"""
    this program defines a class Square with the __init__() method
"""


class Square:
    """
        Square - this class is used to define the square and also
        include an __init__() method which serves to configure the
        object upon instantiation
    """

    def __init__(self, size=0):
        """
            __init__ - this method serves to initialize the objects
            upon instantiation. It also raises some exceptions to
            when some invalid input is given.
            args:
                param1 (int): this is the size and must be an integer
                value unless we want to provoke value error
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("ize must be >= 0")
        self.__size = size

    def area(self):
        """
            area - this method returns the area of the square object
        """

        return (self.__size * self.__size)
