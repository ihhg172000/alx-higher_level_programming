#!/usr/bin/python3
from sys import argv


def print_argv(argv):
    for index in range(1, len(argv)):
        print("{:d}: {:s}".format(index, argv[index]))


if __name__ == "__main__":
    if len(argv) - 1 == 0:
        print("0 arguments.")
    elif len(argv) - 1 == 1:
        print("1 argument:")
        print_argv(argv)
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        print_argv(argv)
