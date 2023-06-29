#!/usr/bin/python3

if __name__ == "__main__":
    """Printing the addition of all arguments."""
    import sys

    total = 0
    for b in range(len(sys.argv) - 1):
        total += int(sys.argv[b + 1])
    print("{}".format(total))
