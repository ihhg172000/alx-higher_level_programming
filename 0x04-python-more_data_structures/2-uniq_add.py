#!/usr/bin/python3
def uniq_add(my_list=[]):
    filtered_list = []
    for num in my_list:
        if num not in filtered_list:
            filtered_list.append(num)
    return sum(filtered_list)
