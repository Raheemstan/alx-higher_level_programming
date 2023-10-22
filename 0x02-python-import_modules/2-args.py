#!/usr/bin/python3
from sys import argv

args = len(argv) - 1

print("{} argument{}:".format(args, 's' if args != 1 else ''))
for i in range(1, args + 1):
    print("{}: {}".format(i, argv[i]))

