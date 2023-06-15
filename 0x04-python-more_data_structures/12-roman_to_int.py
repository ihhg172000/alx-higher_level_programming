#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    numbers = list(map(lambda n: roman_numerals[n], roman_string))
    result_list = []
    result = 0

    for i in range(len(numbers)):
        if numbers[i] <= result:
            result += numbers[i]
        else:
            result = numbers[i] - result
        if i == len(numbers) - 1 or numbers[i + 1] < numbers[i]:
            result_list.append(result)
            result = 0

    return sum(result_list)
