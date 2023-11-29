#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 != 0:
        j = i - 32
    else:
        j = i
    print(chr(j), end='')
