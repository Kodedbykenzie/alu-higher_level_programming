#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or if the object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,
    that inherited from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        bool: True if obj is an instance of or inherited from a_class,
    """
    return isinstance(obj, a_class)
