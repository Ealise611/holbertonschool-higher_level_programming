#!/usr/bin/python3
def safe_print_integer(value):
    if value == None:
        return False
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
