#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    b = 0
    for m in range(x):
        try:
            print(my_list[m], end="")
            b += 1
        except IndexError:
            break
    print()
    return b
