#!/usr/bin/python3
"""
    Class Rectangle: this defines a rectangle
"""


class Rectangle:
    """
        Class Rectangle defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
            this method __ini__ is responsible for setting up
            any instance of this class
            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(width, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
            this method width returns the with attribute of the class
            Returns: width of the triangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """"
            this method sets the value of self.__with to value
            Args: value -> self.__width
            raises: TypeError where value is not an int
                    ValueError where value is -tve
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            this method retrieves the self.__height
            Return: self.__height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
            this method sets the self.__height to value
            Args: value -> self.__height
            raise: TypeError where value is not and int
                    ValueError where value is -tve
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            this method calculates the area of the rectangle
            Return: it returns the result of the calculated area
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
            this method calculates the perimeter of the rectangle
            Return: it returns the result of the calculated perimeter
        """

        return 2 * (self.__width + self.__height)
