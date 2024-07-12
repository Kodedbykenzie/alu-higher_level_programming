#!/usr/bin/python3
"""
Module providing a function to check if an object is an instance
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
