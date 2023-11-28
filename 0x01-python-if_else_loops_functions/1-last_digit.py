#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# check for positivity
if number < 0:
    for_mod = number *- 1
else:
    for_mod = number

# extract the last digit
for_mod %= 10

if number < 0:
    for_mod *= -1

# do the formal printing
print("Last digit of", number, "is", (for_mod), end="")
if (for_mod) > 5:
    print(" and is greater than 5")
elif (for_mod) == 0:
    print(" and is 0")
elif (for_mod < 6) and (for_mod != 0):
    print(" and is less than 6 and not 0")
