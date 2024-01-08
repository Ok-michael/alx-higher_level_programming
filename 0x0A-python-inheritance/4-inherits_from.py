
#!/usr/bin/python3
""" in this module we have a function that checks if an object
is an instance of a class or it's subclass"""

def inherits_from(obj, a_class):
    """ checkss if obj belongs to a_class or it's subclass """
    x = type(obj)
    if x is a_class:
        return False
    if issubclass(x, a_class):
        return True
    return False
