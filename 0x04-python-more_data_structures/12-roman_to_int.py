#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decs = [roman_dictionary[c] for c in roman_string]
    output = 0
    for b in range(len(decs)):
        output += decs[b]
        if decs[b - 1] < decs[b] and b != 0:
            output -= (decs[b - 1] + decs[b - 1])
    return output
