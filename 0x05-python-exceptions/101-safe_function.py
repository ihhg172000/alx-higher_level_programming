#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as msg:
        print("Exception: {}".format(msg), file=stderr)
        return None
