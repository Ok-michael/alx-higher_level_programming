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

    def __init__(self, size=0, position=(0, 0)):
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
        self.position = position

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

    def my_print(self):
        """
            my_print - this method prints a square of size __size to
            the standard output
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

