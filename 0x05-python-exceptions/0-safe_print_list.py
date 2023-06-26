#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
            i = i + 1
        except Exception:
            break
    print("")
    return i
