#!/usr/bin/python3
""" this module has a func that returns the JSON rep of an obj """
import json


def to_json_string(my_obj):
    """ returns a JSON representaton of `my_obj` """
    return json.dumps(my_obj)
