#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def arg_calc(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operation = argv[2]
    b = int(argv[3])
    if operation == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, operation, b, add(a, b)))
    elif operation == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, operation, b, sub(a, b)))
    elif operation == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, operation, b, mul(a, b)))
    elif operation == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, operation, b, div(a, b)))
    else:
        print("Unknown operationerator. Available operationerators:\
                +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    arg_calc(sys.argv)
