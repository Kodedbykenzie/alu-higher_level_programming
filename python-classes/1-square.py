#!/usr/bin/python3
"""
This module defines a class `Square` with a private instance attribute `size`.
"""


class Square:
    """
    This class defines a square with a private instance attribute `size`.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
