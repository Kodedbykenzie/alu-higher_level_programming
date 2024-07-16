#!/usr/bin/python3
"""
Module: 1-write_file
Writes a string to a text file (UTF8) and returns the number of characters
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    Args:
        filename (str): The name of the file to write
        text (str): The string to write to the fil
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
