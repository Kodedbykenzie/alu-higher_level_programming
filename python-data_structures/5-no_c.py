#!/usr/bin/env python3
def no_c(my_string):
    result = []
    for char in my_string:
        if char != 'c' and char != 'C':
            result.append(char)
    return ''.join(result)


# This block is for testing purposes when this script is run directly
if __name__ == "__main__":
    # Test cases as per the example
    print(no_c("Best School"))  # Output: Best Shool
    print(no_c("Chicago"))      # Output: hiago
    print(no_c("C is fun!"))    # Output:  is fun!
