#!/usr/bin/python3
for number in range(100):
    if number < 10:
        print("0{:d} ".format(number), sep=',', end='')
    else:
        print("{:d} ".format(number), sep=',', end='')
