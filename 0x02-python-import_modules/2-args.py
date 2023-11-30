#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    if length == 1:
        print("{:d} arguments.".format(length - 1))
    elif length == 2:
        print("{:d} argument:".format(length - 1))
    else:
        print("{:d} arguments:".format(length - 1))

    i = 1
    for x in sys.argv:
        if x != sys.argv[0]:
            print("{:d}: {:s}".format(i, x))
            i += 1
