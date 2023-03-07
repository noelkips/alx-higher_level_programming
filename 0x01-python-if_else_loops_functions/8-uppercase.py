#!/usr/bin/python3


def uppercase(str):
    for letter in str:
        number = ord(letter)
        if (number >= 97 and number < 123):
            number = number -32
        print(f"{chr(number)}", end='')
    print()

