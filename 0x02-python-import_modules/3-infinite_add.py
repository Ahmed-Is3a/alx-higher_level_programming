#!/usr/bin/python3
import sys


def add_arguments(arguments):
    result = sum(int(arg) for arg in arguments)
    return result


arguments = sys.argv[1:]
total = add_arguments(arguments)
print(total)
