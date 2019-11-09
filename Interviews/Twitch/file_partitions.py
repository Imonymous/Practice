#!/usr/bin/env python3
import sys

def optimalFiles(a, arr):

    if a == 1:
        return sum(arr)
    if len(arr) == 0:
        return 0

    min_so_far = sys.maxsize
    for i in range(1, len(arr)):
        val = min(min_so_far, max(sum(arr[:i]), optimalFiles(a-1, arr[i:])))
        if val < min_so_far:
            min_so_far = val

    return min_so_far

print(optimalFiles(4, [10,30,20,50,40,60]))
