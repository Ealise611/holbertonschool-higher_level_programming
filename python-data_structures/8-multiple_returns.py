#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = ""
    if len(sentence) == 0:
        first = None
    else:
        for i in range(len(sentence)):
            first = sentence[0]
    return length, first
