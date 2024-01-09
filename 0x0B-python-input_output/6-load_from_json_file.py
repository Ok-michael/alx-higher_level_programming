#!/usr/bin/python3
""" this module creates a object from JSON file """
import json


def load_from_json_file(filename):
    """ creates object from JSON file """
    with open(filename, 'r') as file:
        return json.load(file)
