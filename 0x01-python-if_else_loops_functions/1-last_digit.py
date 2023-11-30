#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
if number < 0:
    number = abs(number)
    lastd = (number % 10) * -1
else:
    lastd = number % 10

if lastd > 5:
    print(f"Last digit of {temp} is {lastd} and is greater than 5")
elif lastd < 6 and lastd != 0:
    print(f"Last digit of {temp} is {lastd} and is less than 6 and not 0")
else:
    print(f"Last digit of {temp} is {lastd} and is 0")
