#!/usr/bin/python3


def uppercase(str):
    for letter in str:
        number = ord(letter)
        if (number >= 97 and number < 123):
            number = chr(ord(number) - 32)
        print("{}".format(number), end='')
    print()
