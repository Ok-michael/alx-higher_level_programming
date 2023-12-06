#!/usr/bin/pytho3

def only_diff_elements(set_1, set_2):
    delta = []

    for member in set_1:
        if member not in set_2:
            delta.append(member)

    for member in set_2:
        if member not in set_1:
            delta.append(member)

    return delta
