#!/usr/bin/python3
def is_even(n):
    return True if n % 2 == 0 else False


def divisible_by_2(my_list=[]):
    return list(map(is_even, my_list))
