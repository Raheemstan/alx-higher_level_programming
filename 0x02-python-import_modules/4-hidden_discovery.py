#!/usr/bin/python3
import dis
import hidden_4

names = [name for name in dir(hidden_4) if not name.startswith("__")]
names.sort()
for name in names:
    print(name)
