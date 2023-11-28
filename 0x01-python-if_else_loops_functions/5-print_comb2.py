#!/usr/bin/python3
for number in range(99):
    if number < 10:
        toBePrinted = "0{:d}, ".format(number)
    else:
        toBePrinted = "{:d}, ".format(number)
    print(toBePrinted, end='')
print("{:d}".format(99))
