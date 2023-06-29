#!/usr/bin/python3
from sys import argv
add = 0
for b in argv[1:]:
    add += int(b)
print("{:d}".format(add))
