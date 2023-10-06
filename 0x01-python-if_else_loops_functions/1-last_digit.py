#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

output = "Last digit of " + str(number) + " is " + str(last_digit)

if last_digit > 5:
    output += " and is greater than 5"
elif last_digit == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

print(output)
