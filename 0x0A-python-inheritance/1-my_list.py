#!/usr/bin/python3
"""
    this module houses a class that extends the list class
"""


class MyList(list):
    """ Mylist is gonna extend list and include a couple
    functionalities """
    def __init__(self):
        """ this is the constructor and does the class config"""
        super().__init__()

    def print_sorted(self):
        """ this class prints a sorted version of the list passed """
        print(sorted(self))
