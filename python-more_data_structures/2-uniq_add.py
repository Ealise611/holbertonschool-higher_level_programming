#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = list()
    for num in my_list:
        if num not in unique_list:
            unique_list = unique_list + [num]
    sum = 0
    for nums in unique_list:
        sum += nums
    return sum
