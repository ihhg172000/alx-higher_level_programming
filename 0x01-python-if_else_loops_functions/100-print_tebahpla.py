#!/usr/bin/python3

for ascii in range(122, 96, -1):
    ascii = ascii if ascii % 2 == 0 else ascii - 32
    print("{:c}".format(ascii), end="")
