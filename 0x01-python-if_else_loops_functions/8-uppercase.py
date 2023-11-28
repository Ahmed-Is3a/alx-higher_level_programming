#!/usr/bin/python3
def uppercase(str):
    t = ""
    for i in str:
        a = ord(i)
        if a > 96:
            t = chr(a - 32)
        else:
            t = i

        print("{}".format(t), end="")
    print()
