#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = ""
if number < 0:
    sign = "-"
LD = int(repr(number)[-1])

if LD == 0:
    print(f"Last digit of {number} is {sign}{LD} and is 0")
elif LD > 5:
    print(f"Last digit of {number} is {sign}{LD} and is greater than 5")
elif LD < 6 and not 0:
    print(f"Last digit of {number} is {sign}{LD} and is less than 6 and not 0")
