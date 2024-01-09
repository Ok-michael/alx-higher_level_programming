#!/usr/bin/python3
""" this module has a function that returns an objec in JSON rep """
import json


def from_json_string(my_str):
    """ returns an object in JSON rep """
    return json.loads(my_str)
