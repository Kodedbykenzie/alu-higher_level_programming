#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer


# Test case 1: Normal list
my_list = [1, 2, 3, 4, 5]
print("Testing with normal list:", my_list)
print_reversed_list_integer(my_list)


# Test case 2: None as input
my_list_none = None
print("\nTesting with None:")
print_reversed_list_integer(my_list_none)
