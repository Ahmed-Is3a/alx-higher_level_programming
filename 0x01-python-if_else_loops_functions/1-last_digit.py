#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

LD = int(repr(number)[-1])
if LD == 0:
    print(f"Last digit of {number} is {LD} and is 0")
elif LD > 5:
    print(f"Last digit of {number} is {LD} and is greater than 5")
elif LD < 6 and not 0:
    print(f"Last digit of {number} is {LD} and is less than 6 and not 0")
