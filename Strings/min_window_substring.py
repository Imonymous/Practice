#!/usr/bin/env python3

# Mock 7

"""
Write a function that takes an input string and a character set and returns the
minimum-length substring which contains every letter of the character set at
least once, in any order.

If you don't find a match, return an empty string.

a - 7
b - 11
c - 6
s - 9
"""

import sys

def reset(d):
    for i in d.keys():
        d[i] = 0

def check_seen(d):
    for i in d.keys():
        if d[i] == 0:
            return False
    return True

def get_min_ss(inp, char_set):
    d = dict()

    min_start = 0
    min_end = len(inp)

    start_idx = 0
    end_idx = -1

    min_ss = sys.maxsize
    pos = 0

    while pos < len(inp):

        if inp[pos] in char_set:

            if inp[pos] in d.keys():
                d[inp[pos]] += 1
            else:
                d[inp[pos]] = 1

            if check_seen(d):
                end_idx = pos

                while check_seen(d):
                    if inp[start_idx] in d.keys():
                        d[inp[start_idx]] -= 1
                    start_idx += 1
                print(inp[start_idx-1:end_idx+1])
        pos += 1

    return end_idx+1-start_idx+1

print(get_min_ss("aaaaaaaaaabbbbbbbbcccccscccbabsbccc", {'a', 'b', 'c', 's'}))
