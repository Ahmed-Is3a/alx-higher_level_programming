#!/usr/bin/python3

def print_last_digit(number):
    LD = int(repr(number)[-1])
    print("{}".format(LD), end="")
    return (LD)
