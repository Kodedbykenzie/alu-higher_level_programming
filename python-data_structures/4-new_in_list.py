#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list
    # Create a new list with the modified element
    new_list = my_list[:]
    new_list[idx] = element
    return new_list


# This block is for testing purposes when this script is run directly
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)
    print(new_list)  # Print the modified list
    print(my_list)   # Print the original list
