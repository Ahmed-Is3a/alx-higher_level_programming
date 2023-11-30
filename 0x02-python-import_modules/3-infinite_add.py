#!/usr/bin/python3
import sys

if __name__ == "__main__":

    def add_arguments(arguments):
        result = sum(int(arg) for arg in arguments)
        return result

    arguments = sys.argv[1:]
    total = add_arguments(arguments)
    print(total)
