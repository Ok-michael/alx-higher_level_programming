#!/usr/bin/python3
lower_alphabets = ""
for i in range(97, 123):
    if chr(i) != 'e' and chr(i) != 'q':
        lower_alphabets += chr(i)
print("{:s}".format(lower_alphabets), end='')
