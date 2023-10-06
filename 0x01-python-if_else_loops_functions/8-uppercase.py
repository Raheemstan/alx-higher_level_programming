#!/usr/bin/python3

def uppercase(str):
    word = ''
    for char in str:
        ascii_value = ord(char)
        if ord('a') <= ascii_value <= ord('z'):
            word += chr(ascii_value - 32)
        else:
            word += char

    print("{}".format(word), end='\n')
