#!/usr/bin/python3
"""This module defines a class BaseGeometry"""


class BaseGeometry:
    """ this class defines a BaseGeometry with some methods """

    def area(self):
        """ this method simply raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this method validates value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ this class extends BaseGeometry and further implements some
        methods """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ this method evaluates the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ it is a custom string representation of the rectangle """
        return f'[Rectangle] {self.__width}/{self.__height}'
