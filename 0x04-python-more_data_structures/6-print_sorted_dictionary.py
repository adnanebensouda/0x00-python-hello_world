#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for pas in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(pas, a_dictionary[pas]))
