#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set(my_list)
    sigma = 0
    for member in uniq:
        sigma += member
    return sigma
