#!/usr/bin/python3

def search_replace(my_list, search, replace):
    delta_list = []
    for elem in my_list:
        if elem == search:
            delta_list.append(replace)
        else:
            delta_list.append(elem)
    return (delta_list)
