#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list[:]
    if idx >= 0 and idx < len(copied_list):
        copied_list[idx] = element
    return copied_list
