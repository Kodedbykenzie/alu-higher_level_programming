#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2 == 0):
        letter = chr(i)
    else:
        letter = chr(i).upper()
    print("{}".format(letter), end="")
