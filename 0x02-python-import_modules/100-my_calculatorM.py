#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = "+-*/"
    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif op == '-':
        print("{:d} + {:d} = {:d}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{:d} + {:d} = {:d}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{:d} + {:d} = {:d}".format(a, b, div(a, b)))
