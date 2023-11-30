#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    arguments = argv[1:]
    n = len(argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))

    for i in range(n):
        print("{}: {}".format(i + 1, arguments[i]))
