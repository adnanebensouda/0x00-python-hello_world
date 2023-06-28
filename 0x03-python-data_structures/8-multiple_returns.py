#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuples = ()
    if len(sentence) == 0:
        my_tuples = 0, "None"
    else:
        my_tuples = len(sentence), sentence[0]
    return my_tuples
