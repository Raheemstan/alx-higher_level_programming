#!/usr/bin/python3
from sys import argv

args = argv[1:]

if args:
    result = sum(map(int, args))
    print(result)
else:
    print(0)

