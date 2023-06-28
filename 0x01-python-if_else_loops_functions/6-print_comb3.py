#!/usr/bin/python3
for m in range(0, 8):
    for j in range(m + 1, 10):
        print("{:d}{:d}".format(m, j), end=', ')
print("{:d}{:d}".format(m + 1, j))
