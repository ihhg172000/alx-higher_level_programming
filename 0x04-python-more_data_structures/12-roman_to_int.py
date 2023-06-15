#!/usr/bin/python3
from functools import reduce

roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman(a, b):
    if a in roman_numerals:
        a = roman_numerals[a]
    if b in roman_numerals:
        b = roman_numerals[b]
    if a > b or a == b:
        return a + b
    return b - a


def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    if roman_string in roman_numerals:
        return roman_numerals[roman_string]
    return reduce(roman, roman_string)
