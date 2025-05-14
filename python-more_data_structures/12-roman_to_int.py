#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    if len(roman_string) < 0:
        return None
    if not isinstance(roman_string, str):
        return None
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman[roman_string[i]] < roman[roman_string[i + 1]]:
            result += roman[roman_string[i + 1]] - roman[roman_string[i]]
            i += 1
        else:
            result += roman[roman_string[i]]
        i += 1
    return result