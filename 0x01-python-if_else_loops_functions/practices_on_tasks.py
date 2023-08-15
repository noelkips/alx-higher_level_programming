#!/usr/bin/python3
"""
# Task 1
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    print(f"last digit {last_digit} is greater than 5")
elif last_digit == 0:
    print(f"last digit {last_digit} is zero")
elif last_digit < 6 and last_digit != 0:
    print(f"{last_digit}  is less than 6 and not 0")"


#Task 2
for i in range(97, 123, 1):
    print(chr(i), end="")


#Task 3
for i in range(97, 123, 1):
    if chr(i) == "q" or chr(i) == "e":
        continue
    print(chr(i), end="")


#Task 4
for i in range(0, 99):
    print(f"{i} = {hex(i)}")

#Task 5
for i in range(100):
    if i == 99:
        print(i)
    else:
        print("{:0>2}, ".format(i), end="")

#Task 6

for i in range(10):
    for x in range(10):
        if int(str(i) + str(x)) < int(str(x) + str(i)):
            if int(str(i) + str(x)) == 89:
                print(f"{i}{x}")
            else:
                print(f"{i}{x}, ", end="")

#Task 7
def islower(c):
     letter = ord(c)
     if letter in range(97,123):
         return True
     else:
         return False

letter = input("Enter letter: ")
c = islower(letter)
print("{} is {}".format(letter, "Lower" if c == True else "Upper"))
"""
#task 8:

def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            i = chr(ord(i) - 32)
        print(f"{i}", end="")
    print()

uppercase("best")
uppercase("Best School 98 Battery street")

