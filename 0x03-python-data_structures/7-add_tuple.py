#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_0 = (tuple_a + (0, ))[0] + (tuple_b + (0, ))[0]
    sum_1 = (tuple_a + (0, 0))[1] + (tuple_b + (0, 0))[1]
    return (sum_0, sum_1)
