#!/usr/bin/python3

def no_c(my_string):
    if not my_string:
        return

    new_string = ""
    for character in my_string:
        if character not in  'cC':
            new_string += character

    return (new_string)
