#!/usr/bin/python3
def roman_to_int(roman_string):
    r = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
    result = 0
    i = 0
    if not isinstance(roman_string, str):
        return 0
    while i < len(roman_string):
        if (
            i + 1 < len(roman_string) 
            and r[roman_string[i]] < r[roman_string[i + 1]]
            ):
            result += r[roman_string[i + 1]] - r[roman_string[i]]
            i += 1
        else:
            result += r[roman_string[i]]
        i += 1
    return result
