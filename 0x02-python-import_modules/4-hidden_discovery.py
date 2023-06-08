#!/usr/bin/python3
import hidden_4


def print_names(module):
    for name in dir(module):
        if name[:2] != "__":
            print("{:s}".format(name))


if __name__ == "__main__":
    print_names(hidden_4)
