#!/usr/bin/python3
def uniq_add(my_list=[]):
    ad = 0
    for f in set(my_list):
        ad += f
    return ad
