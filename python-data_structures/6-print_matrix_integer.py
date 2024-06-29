#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Print each element of the row followed by a space
            print("{:d}".format(row[i]), end=" ")
        print()  # Move to the next line after printing each row


# This block is for testing purposes when this script is run directly
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
