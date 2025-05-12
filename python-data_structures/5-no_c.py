#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for chars in my_string:
        if chars != "c" and chars != "C":
            result += chars
    return result
