#!/usr/bin/python3
"""
nqueens backtrack program to print the coordinates of n queens
on an nxn that they are all in non-attack positioning
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for v in range(n):
        a.append([v, None])

    def already_exists(y):
        """check that a queen does not already exist in that y value"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """determines whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        v = 0
        while(v < x):
            if abs(a[v][1] - y) == abs(v - x):
                return False
            v += 1
        return True

    def clear_a(x):
        """clears the answers from the point of failure on"""
        for v in range(x, n):
            a[v][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1):  # accepts the solutions
                    print(a)
                else:
                    nqueens(x + 1)  # moves on to next x value to continue

    # start the recursive processing at x = 0
    nqueens(0)
