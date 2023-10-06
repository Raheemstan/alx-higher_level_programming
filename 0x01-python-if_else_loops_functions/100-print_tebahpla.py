#!/usr/bin/python3

for i in range(25, -1, -1):
    print("{:c}".format(i + ord('a')).upper()
          if i % 2 == 0 else "{:c}".format(i + ord('a')), end='')
