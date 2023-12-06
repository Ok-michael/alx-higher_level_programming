#!/usr/bin/python3

def common_elements(set_1, set_2):
    interception = []
    for member in set_1:
        if member in set_2:
            interception.append(member)
    return (interception)
