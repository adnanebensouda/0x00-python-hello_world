#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for a in range(0, len(my_list)):
        if my_list[a] % 2 == 0:
            new_list[a] = 1
        else:
            new_list[a] = 0
    return new_list
