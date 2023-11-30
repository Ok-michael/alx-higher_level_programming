#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0
    if len(sys.argv) > 1:
        for arg in sys.argv:
            if arg != sys.argv[0]:
                result += int(arg)

    print(result)
