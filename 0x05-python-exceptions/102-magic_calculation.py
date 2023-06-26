#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    for r in range(1, 3):
        try:
            if r > a:
                raise Exception('Too far')

            result += a ** b / r
        except:
            result = b + a
            break

    return result
