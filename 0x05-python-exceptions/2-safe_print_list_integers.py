#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count = count + 1
        except (TypeError, ValueError):
            continue
        finally:
            i = i + 1
    print("")
    return count
