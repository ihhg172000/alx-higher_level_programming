#!/usr/bin/python3
def weight_average(my_list=[]):
    s = sum(list(map(lambda item: item[0] * item[1], my_list)))
    w = sum(list(map(lambda item: item[1], my_list)))
    return s / w
