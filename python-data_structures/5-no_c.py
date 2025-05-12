#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == "c":
            index_c = i
            return my_string[:index_c] + my_string[index_c + 1:]
    return my_string
