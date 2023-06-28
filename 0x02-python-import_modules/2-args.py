#!/usr/bin/python3

import sys

counte = len(sys.argv) - 1
if counte == 0:
    print("0 arguments.")
elif counte == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(counte))
for j in range(counte):
     print("{}: {}".format(j + 1, sys.argv[j + 1]))
