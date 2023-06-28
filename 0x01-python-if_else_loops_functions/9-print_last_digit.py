#!/usr/bin/python3
def print_last_digit(number):
    '''printing the last digit of a numbers'''
    last_di = abs(number) % 10
    print(f"{last_di}", end='')
    return last_di
