#!/usr/bin/python3

def safe_print_division(a, b):
    p = None
    try:
        p = a / b
    except (ZeroDivisionError):
        return None
    finally:
        print("Inside result: {}".format(p))
        return p
