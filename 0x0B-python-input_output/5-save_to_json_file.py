#!/usr/bin/python3
""" write an objec to a text file using JSON """
import json


def save_to_json_file(my_obj, filename):
    """ writes and object toa text file using JSON rep """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
