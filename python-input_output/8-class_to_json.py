#!/usr/bin/python3
"""
Module: 8-class_to_json
Converts an instance of a class into a dictionary description for JSON
"""


def class_to_json(obj):
    """Converts an instance of a class into a dictionary suitable for JSON
    Args:
        obj (object): An instance of a class with attributes that are JSON
    Returns:
        dict: A dictionary representation of the object suitable for JSON
    """
    attributes = obj.__dict__.copy()  # Get instance attributes dictionary
    # Handle private attributes (name mangled in Python)
    for key in attributes:
        if key.startswith("__") and not key.endswith("__"):
            attributes[key] = getattr(obj, key)
    # Exclude methods and non-serializable attributes
    attributes = {key: val for key, val in attributes.items()
                  if isinstance(val, (list, dict, str, int, bool))}
    return attributes
