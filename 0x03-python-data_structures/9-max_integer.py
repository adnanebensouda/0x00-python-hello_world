#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    large = my_list[0]
    for j in range(1, len(my_list)):
        if large < my_list[j]:
            large = my_list[j]
        else:
            continue
    return large
