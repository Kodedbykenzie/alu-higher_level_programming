#!/usr/bin/python3
"""
Module: 2-append_write
Appends a string to a text file (UTF8).
"""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns the number of character
    Args:
        filename (str): The file name. Defaults to an empty string.
        text (str): The string to append. Defaults to an empty string
    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
