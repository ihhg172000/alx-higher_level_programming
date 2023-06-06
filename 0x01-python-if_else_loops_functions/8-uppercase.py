#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        ascii = ord(letter)
        if ascii >= 97 and ascii <= 122:
            ascii -= 32
        print("{:c}".format(ascii), end="")
    print("")
