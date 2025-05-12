#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp_a = list(tuple_a)
    temp_b = list(tuple_b)
    while len(temp_a) < 2:
        temp_a.append(0)
    while len(temp_b) < 2:
        temp_b.append(0)
    return temp_a[0] + temp_b[0], temp_a[1] + temp_b[1]
