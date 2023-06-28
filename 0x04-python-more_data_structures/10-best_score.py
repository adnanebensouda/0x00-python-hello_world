#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        top = list(a_dictionary.keys())[0]
        for top in a_dictionary:
            if a_dictionary[key] > a_dictionary[top]:
                top = key
        return top
    return None
