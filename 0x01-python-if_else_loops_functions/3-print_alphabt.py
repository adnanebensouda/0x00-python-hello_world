#!/usr/bin/python3
for alphab in range(97, 123):
    if chr(alphab) == 'q' or chr(alphab) == 'e':
        continue
    print(chr(alphab).format(alphab), end='')
