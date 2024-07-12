#!/usr/bin/python3
"""
Module: 1-my_list
Defines a MyList class that inherits from list and includes a method to print
"""


class MyList(list):
    """
    A class that inherits from list and adds a method to print the list

    Methods
    -------
    print_sorted(self)
        Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
